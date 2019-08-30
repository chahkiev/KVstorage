import unittest
import json
import requests


class TestPOSTMethod(unittest.TestCase):

    def test_POST_OK(self):
        url = 'http://localhost:8000/kv/'
        requestData = {"key" : "tarantul", "value" : {"mail": "ru", "group" : "company"}}
        jsn = json.dumps(requestData)
        r = requests.post(url, data  = jsn )
        self.assertEqual(str(r), '<Response [200]>')

    def test_POST_BAD_REQUEST(self):
        url = 'http://localhost:8000/kv/'
        requestData = {"key" : "tarantul", "bad_value" : {"mail": "ru", "group" : "company"}}
        jsn = json.dumps(requestData)
        r = requests.post(url, data  = jsn )
        self.assertEqual(str(r), '<Response [400]>')

    def test_POST_CONFLICT(self):
        url = 'http://localhost:8000/kv/'
        requestData = {"key" : "tarantul", "value" : {"mail": "ru", "group" : "company"}}
        jsn = json.dumps(requestData)
        r = requests.post(url, data  = jsn )
        self.assertEqual(str(r), '<Response [409]>')


class TestPUTMethod(unittest.TestCase):

    def test_PUT_OK(self):
        url = 'http://localhost:8000/kv/tarantul/'
        requestData = {"value" : {"men": "2", "women" : "4"}}
        jsn = json.dumps(requestData)
        r = requests.put(url, data  = jsn )
        self.assertEqual(str(r), '<Response [200]>')

    def test_PUT_BAD_REQUEST(self):
        url = 'http://localhost:8000/kv/tarantul/'
        requestData = {"bad_value" : {"men": "2", "women" : "4"}}
        jsn = json.dumps(requestData)
        r = requests.put(url, data  = jsn )
        self.assertEqual(str(r), '<Response [400]>')

    def test_PUT_NOT_FOUND(self):
        url = 'http://localhost:8000/kv/non_existent_key/'
        requestData = {"value" : {"men": "2", "women" : "4"}}
        jsn = json.dumps(requestData)
        r = requests.put(url, data  = jsn )
        self.assertEqual(str(r), '<Response [404]>')


class TestGETMethod(unittest.TestCase):

    def test_GET_OK(self):
        url = 'http://localhost:8000/kv/tarantul/'
        r = requests.get(url)
        self.assertEqual(str(r), '<Response [200]>')

    def test_GET_NOT_FOUND(self):
        url = 'http://localhost:8000/kv/non_existent_key/'
        r = requests.get(url)
        self.assertEqual(str(r), '<Response [404]>')


class TestDELETEMethod(unittest.TestCase):

    def test_GET_NOT_FOUND(self):
        url = 'http://localhost:8000/kv/non_existent_key/'
        r = requests.delete(url)
        self.assertEqual(str(r), '<Response [404]>')

    def test_GET_OK(self):
        url = 'http://localhost:8000/kv/tarantul/'
        r = requests.delete(url)
        self.assertEqual(str(r), '<Response [200]>')



if __name__ == '__main__':
    unittest.main()
