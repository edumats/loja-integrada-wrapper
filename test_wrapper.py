import os
import unittest
from unittest.mock import Mock, patch
from requests.exceptions import HTTPError

from wrapper import LojaIntegrada as LI
from wrapper import APIKeyMissingError
from helpers import mock_customer_response, mock_brands_response

requests = Mock()


class TestWrapper(unittest.TestCase):
    def setUp(self):
        self.wrapper = LI()

    def test_init(self):
        """ Test if environment variables are correctly initialized """

        self.assertEqual(self.wrapper.api_key, os.environ['API_KEY'])
        self.assertEqual(self.wrapper.app_key, os.environ['APP_KEY'])

        # Tests if error is raised if API key is not present
        with patch.dict(os.environ, {'API_KEY': ''}):
            with self.assertRaises(APIKeyMissingError):
                LI()
        # Tests if error is raised if APP key is not present
        with patch.dict(os.environ, {'APP_KEY': ''}):
            with self.assertRaises(APIKeyMissingError):
                LI()

    def test_url_builder(self):
        """ Test if generated url is the expected one """

        self.assertEqual(
            self.wrapper._url('cliente'),
            'https://api.awsli.com.br/v1/cliente/'
        )
        self.assertIsInstance(self.wrapper._url('cliente'), str)

    @patch('wrapper.requests.get')
    def test_call_get(self, mock_get):
        """ Test GET call method """
        mock_get.return_value.status_code = 200

        response = self.wrapper._call_get('marca')
        self.assertEqual(response.status_code, 200)

        mock_get.side_effect = HTTPError

        with self.assertRaises(SystemExit):
            self.wrapper._call_get('marca')

    @patch('wrapper.requests.post')
    def test_call_post(self, mock_post):
        """ Test _call_post method """
        payload = {'data': 1}

        mock_post.side_effect = HTTPError

        with self.assertRaises(SystemExit):
            self.wrapper._call_post('cliente', payload)

        # Set to None to clear the previous side effect
        mock_post.side_effect = None
        mock_post.return_value.status_code = 200

        response = self.wrapper._call_post('cliente', payload)
        self.assertEqual(response.status_code, 200)

    @patch('wrapper.requests.post')
    def test_create_customer(self, mock_post):
        """ Test create customer method """

        mock_post.return_value.json.return_value = mock_customer_response
        customer = self.wrapper.create_customer()
        self.assertIsInstance(customer, dict)

    @patch('wrapper.requests.get')
    def test_get_brands(self, mock_get):
        """ Test get all brands """
        mock_get.return_value.json.return_value = mock_brands_response
        brands = self.wrapper.get_brands()
        self.assertIsInstance(brands, dict)


if __name__ == '__main__':
    unittest.main()
