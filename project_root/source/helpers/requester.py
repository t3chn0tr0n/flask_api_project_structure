"""
    A Module to implement requests to make a Post request!
    Handels Errors and returns False if error occurs, else returns responce object!
"""
import requests
from requests.exceptions import ConnectionError

from . import app


def connect_api(api_url: str, api_port: str, end_point: str, data: dict):
    """
        :params:
         * api_url: str
         * api_port: str
         * end_point: str
         * data: dict

        :returns:
         * responce obj
         * False: if error occurs
    """
    try:
        url = "".join([api_url, ":", str(api_port), end_point])
        response = requests.post(url, json=data)
        return response
    except ConnectionError:
        app.logger.error("ConnectionError: %s", api_url)
        return False
    except Exception as e:
        app.logger.error(e)
        return False
