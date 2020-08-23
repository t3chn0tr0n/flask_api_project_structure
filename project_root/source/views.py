import re
from datetime import datetime, timedelta
from uuid import uuid4

from flask import Response, jsonify, request

from .. import BOUNCER, app
from ..config import DEBUG
from .auth import required_fields
from .db.models import DemoModel

validate_request = BOUNCER.validate_request


# --- Format ---

# @validate_request() # for log-in required apis
# @required_fields(required={"POST": ["field1", "field2"]}, remove_excess=True) # To check if all required fields are present or not!
# def func():
#     pass


def check():
    app.logger.info("OK")
    return "yes!"
