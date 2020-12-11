import unittest
import requests
import urllib.parse
import json


class BackendTestCases(unittest.TestCase):
    def test_checkAuth_True(self):
        base_url = 'http://localhost:5000/checkAuth'
        headers = {'Authorization': 'Authorized'}

        response = requests.get(base_url, headers)
        self.assertTrue(response)


    def test_checkAuth_noHead(self):
        base_url = 'http://localhost:5000/checkAuth'
        headers = {}

        response = requests.get(base_url, headers).json()
        self.assertFalse(response)


    def test_checkAuth_wrongValue(self):
        base_url = 'http://localhost:5000/checkAuth'
        headers = {'Authorization': 'Not Authorized'}

        response = requests.get(base_url, headers).json()
        self.assertFalse(response)


    def test_checkAuth_wrongHead(self):
        base_url = 'http://localhost:5000/checkAuth'
        headers = {'TestCase': 'Authorized'}

        response = requests.get(base_url, headers).json()
        self.assertFalse(response)


    def test_saveAPIResponse(self):
        base_url = 'http://localhost:5000/saveResponse?'
        url_vars = {'url': 'https://ghibliapi.herokuapp.com/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49',
                    'path': 'C:/Users/Jerry/Desktop/veerassessment/flask-api'}

        url = base_url + urllib.parse.urlencode(url_vars)
        actual_response = requests.get(url).text
        expected_response = 'Data Saved to ' + url_vars['path'] + '/apiresponse.json'

        self.assertEqual(actual_response, expected_response)


    def test_saveAPIResponse_noPath(self):
        base_url = 'http://localhost:5000/saveResponse?'
        url_vars = {'url': 'https://ghibliapi.herokuapp.com/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49'}

        url = base_url + urllib.parse.urlencode(url_vars)
        actual_response = requests.get(url).text
        expected_response = 'You need a "url" and "path" parameter.'

        self.assertEqual(actual_response, expected_response)


    def test_saveAPIResponse_noURL(self):
        base_url = 'http://localhost:5000/saveResponse?'
        url_vars = {'path': 'C:/Users/Jerry/Desktop/veerassessment/flask-api'}

        url = base_url + urllib.parse.urlencode(url_vars)
        actual_response = requests.get(url).text
        expected_response = 'You need a "url" and "path" parameter.'

        self.assertEqual(actual_response, expected_response)


    def test_saveAPIResponse_noParams(self):
        base_url = 'http://localhost:5000/saveResponse?'
        url_vars = {}

        url = base_url + urllib.parse.urlencode(url_vars)
        actual_response = requests.get(url).text
        expected_response = 'You need a "url" and "path" parameter.'

        self.assertEqual(actual_response, expected_response)


    def test_saveAPIResponse_wrongParams(self):
        base_url = 'http://localhost:5000/saveResponse?'
        url_vars = {'something': 'https://ghibliapi.herokuapp.com/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49',
                    'somethingElse': 'C:/Users/Jerry/Desktop/veerassessment/flask-api'}

        url = base_url + urllib.parse.urlencode(url_vars)
        actual_response = requests.get(url).text
        expected_response = 'You need a "url" and "path" parameter.'

        self.assertEqual(actual_response, expected_response)


    def test_saveAPIResponse_invalidURl(self):
        base_url = 'http://localhost:5000/saveResponse?'
        url_vars = {'url': 'https://ghibliapi.herokuapp.com/films/58611129-2dbc-4a81-a72fb4',
                    'path': 'C:/Users/Jerry/Desktop/veerassessment/flask-api'}

        url = base_url + urllib.parse.urlencode(url_vars)
        actual_response = requests.get(url).text
        expected_response = 'Invalid URL'

        self.assertEqual(actual_response, expected_response)


    def test_saveAPIResponse_invalidPath(self):
        base_url = 'http://localhost:5000/saveResponse?'
        url_vars = {'url': 'https://ghibliapi.herokuapp.com/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49',
                    'path': 'C:/Users/Jerry/Desktop/vk-api'}

        url = base_url + urllib.parse.urlencode(url_vars)
        actual_response = requests.get(url).text
        expected_response = 'Invalid Path'

        self.assertEqual(actual_response, expected_response)

    def test_saveAPIResponse_invalidParamValues(self):
        base_url = 'http://localhost:5000/saveResponse?'
        url_vars = {'url': 'https://ghibliapi.herokuapp.com/fila72f-77ddfc1b1b49',
                    'path': 'C:/Users/Jerry/Desktop/vk-api'}

        url = base_url + urllib.parse.urlencode(url_vars)
        actual_response = requests.get(url).text
        expected_response = 'Invalid URL'

        self.assertEqual(actual_response, expected_response)


if __name__ == '__main__':
    unittest.main()
