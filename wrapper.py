import os
import requests

from ratelimit import limits, sleep_and_retry

REQUESTS_TIMEOUT = 10


class APIKeyMissingError(Exception):
    """
    Raised when there is no API key in TINY_TOKEN_KEY environment variable
    """
    pass


class LojaIntegrada:
    def __init__(self):
        # Tries to get Loja Integrada's keys from environment variable
        API_KEY = os.environ.get('API_KEY', None)
        APP_KEY = os.environ.get('APP_KEY', None)

        if not API_KEY:
            raise APIKeyMissingError(
                'Loja Integrada API key not found. '
                'Check if it is defined as an environment variable.'
            )

        if not APP_KEY:
            raise APIKeyMissingError(
                'Loja Integrada APP key not found. '
                'Check if it is defined as an environment variable.'
            )

        # Sets API key
        self.api_key = API_KEY

        # Sets APP key
        self.app_key = APP_KEY

        # Sets requests timeout to x seconds
        self.timeout = REQUESTS_TIMEOUT

    def _url(self, url: str) -> str:
        """ Given a url path, returns a complete url to make the API call """
        return f'https://api.awsli.com.br/v1/{url}/'

    def _call_post(self, path: str, payload: dict):
        """ Calls a POST request given a path and a dict payload """
        headers = {
            'Authorization': f"chave_api {self.api_key} aplicacao {self.app_key}"
        }

        try:
            response = requests.post(self._url(path), json=payload, headers=headers)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

        return response

    def _call_get(self, path: str):
        """ Calls a GET request given a path """
        data = {
            'format': 'json',
            'chave_api': {self.api_key},
            'chave_aplicacao': {self.app_key}
        }

        try:
            response = requests.get(self._url(path), params=data)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

        return response

    def create_customer(self, **kwargs):
        """ Creates a customer in shop by calling an external API """

        response = self._call_post('cliente', kwargs)
        return response.json()

    def get_brands(self):
        """ Get all brands from shop by calling the external API """

        response = self._call_get('marca')
        return response.json()
