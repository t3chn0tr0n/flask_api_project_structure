from logging.config import dictConfig

from flask import Flask
from flask_cors import CORS

from .config import (
    CORS_ORIGINS, CUR_DIR, MEM_COST, OBJ_POOL_COUNT, PARALLEL, PASS_HASH_LEN,
    PASS_SALT_LEN, SECRET_KEY, TIME_COST, TOKEN_EXP_MINUTES)

app = Flask(__name__)  # Flask Object
cors = CORS(app, resources=CORS_ORIGINS)  # SETTING CORS POLICY


dictConfig({
    'version': 1,
    'formatters': {'default': {
        # For Time: %(asctime)s
        # For Level (ERROR, INFO, etc): %(levelname)s
        # For Module name (usually file name): %(module)s
        # For Line No: %(funcName)s
        # For Message: %(message)s
        # For Process Id and Name: %(process)s, %(processName)s
        # For Thread Id and Name: %(thread)s, %(threadName)s
        'format': '[%(asctime)s]|%(levelname)s|%(module)s|%(funcName)s|%(lineno)s|%(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


# ---- DO NOT MOVE THE BELLOW CODES TO TOP -----
from .source.auth import AuthAndToken

# SETTING UP AUTH BOUNCER
BOUNCER = AuthAndToken(
    SECRET_KEY,
    token_exp_in_minutes=TOKEN_EXP_MINUTES,
    hash_len=PASS_HASH_LEN,
    salt_len=PASS_SALT_LEN,
    parallelism=PARALLEL,
    time_cost=TIME_COST,
    memory_cost=MEM_COST,
)

from .source.urls import *
