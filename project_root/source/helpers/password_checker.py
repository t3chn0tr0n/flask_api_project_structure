import re


def password_check(password):
    while True:
        if len(password) < 8:
            return {"error": True, "message": "Password less than 8 characters!"}
        if len(password) > 100:
            return {"error": True, "message": "Password more than 100 characters!"}
        elif not re.search("[a-z]", password):
            return {"error": True, "message": "Password does not have at least one small letter!"}
        elif not re.search("[A-Z]", password):
            return {"error": True, "message": "Password does not have at least one Capital letter!"}
        elif not re.search("[0-9]", password):
            return {"error": True, "message": "Password does not have at least one digit!"}
        elif not re.search("[_@$%&!/^|*#`~]", password):
            return {
                "error": True,
                "message": "Password does not have at least one special character (_,@,$,%,&,!,/,^,|,*,#,`,~)!"
            }
        elif re.search("\s", password):
            return {"error": True, "message": "Password has space!"}
        else:
            return {"error": False, "message": "Password Valid!"}
