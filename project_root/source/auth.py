"""
    Authentication Module - Implements argon2
"""
import datetime
import functools

import jwt
from argon2 import PasswordHasher
from argon2.exceptions import VerificationError, VerifyMismatchError
from flask import request


def __check_required_fields(rqd_fields, request_body):
    absent = ""
    for field in rqd_fields:
        value = request_body.get(field) if type(
            field) is str else request_body.get(field)
        if not value:
            absent += "'" + field + "'" + ", "
        else:
            request_body[field] = value
    if absent != '':
        return absent[:-2]
    return False


def required_fields(required=None, remove_excess=False):
    """
    Decorator: Checks if all fields mentioned are present and strips them
    :param:
     * Dictionary of format: {<request_method> : [list of required fields]} => eg: {"POST": ["id", "password"]}
    """
    if required is None:
        required = {}

    def wrapper_layer2(func):
        @functools.wraps(func)
        def wrapper_layer1(*args, **kws):
            if request.method in required.keys():
                fields = required.get(request.method)
                data = request.json
                if not data:
                    return {"success": False, 'error': "No request body received"}, 400

                fields_absent = __check_required_fields(fields, data)
                if fields_absent:
                    return {"success": False, 'error': "All fields required! Missing: " + fields_absent}, 400
                if remove_excess:
                    fields = list(data.keys())
                    for field in fields:
                        if field not in required.get(request.method):
                            del data[field]
            return func(*args, **kws)
        return wrapper_layer1
    return wrapper_layer2


class AuthAndToken:
    def __init__(self, sec_key, token_exp_in_minutes=60, time_cost=2, memory_cost=102400, parallelism=8, hash_len=16, salt_len=16):
        self.ph = PasswordHasher(
            time_cost, memory_cost, parallelism, hash_len, salt_len)
        self.secret_key = sec_key
        self.token_exp = token_exp_in_minutes

    def __verify_user(self, token):
        """
            receives a jwt token and verifies it's parameters
        """
        key = str(self.secret_key)
        try:
            jwt.decode(token, key, algorithms=['HS256'])
        except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
            return False
        return True

    def create_password(self, password):
        password = self.ph.hash(password)
        return password

    def verify_password(self, given_password, hash_password):
        """
            Validates if a password is valid or not and checks if rehashing is required or not(if valid)
            :param:
             * username
             * supplied password
            
            :returns:
             * validation status (True/False)
             * updated password(if needed) else ''
        """
        try:
            if self.ph.verify(hash_password.encode('utf-8'), given_password):
                if self.ph.check_needs_rehash(hash_password):
                    # rehash password if needed
                    hash_password = self.ph.hash(given_password)
                    return True, hash_password
            return True, ''
        except (VerificationError, VerifyMismatchError):
            return False, ''

    def validate_request(self, required=None, token_name='token'):
        """
            Decorator for validating Token and all required fields for a request
            :param:
             * required fields (if any): Dictionary of format:
                {<request_method> : [list of required fields]} => eg: {"POST": ["id", "password"]}
             * token name used in the header [default is 'token']
        """
        if required is None:
            required = {}

        def wrapper_layer2(func):
            @functools.wraps(func)
            @required_fields(required=required)
            def wrapper_layer1(*args, **kws):
                # checking JWT token
                token = request.headers.get(token_name)
                if not token:
                    return {'error': True, "message": "Token Required!", "token404": True}, 401
                if not self.__verify_user(token):
                    return {'error': True, "message": "Invalid Token. Try logging in!", "unauth":  True}, 403

                return func(*args, **kws)
            return wrapper_layer1
        return wrapper_layer2

    def get_token(self, user):
        """
            Generates a new JWT
        """
        key = str(self.secret_key)
        claims = {
            'user': user,
            'time': str(datetime.datetime.utcnow()),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=self.token_exp),
        }
        return jwt.encode(claims, key, algorithm='HS256')

    def get_user(self, token):
        claims = jwt.decode(token, verify=False)
        return str(claims['user'])
