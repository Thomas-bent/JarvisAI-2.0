"""

import requests
from requests import Response
from config_files import config


def post(url: str, body: dict):
    return requests.post(config.backend.URL + url, json=body).json()


def get(url: str):
    return requests.get(config.backend.URL + url)


print(get('/contacts'))"""