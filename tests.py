import unittest
import json
import requests


class TestPOSTMethod(unittest.TestCase):

    def test_POST_OK(self):
        url = 'http://localhost:8000/kv/'
        requestData = {"key" : "black_widow", "value" : {"mail": "ru", "group" : "company"}}
        jsn = json.dumps(requestData)
        r = requests.post(url, data  = jsn )
        self.assertEqual(str(r), '<Response [200]>')

        url = 'http://localhost:8000/kv/black_widow/'  # deleting 'black_widow' record
        requests.delete(url)                           #

    def test_POST_BAD_REQUEST(self):
        url = 'http://localhost:8000/kv/'
        requestData = {"key" : "hermit", "bad_value" : {"mail": "ru", "group" : "company"}}
        jsn = json.dumps(requestData)
        r = requests.post(url, data  = jsn )
        self.assertEqual(str(r), '<Response [400]>')

    def test_POST_CONFLICT(self):
        url = 'http://localhost:8000/kv/'
        requestData = {"key" : "robber", "value" : {"mail": "ru", "group" : "company"}}
        jsn = json.dumps(requestData)
        r = requests.post(url, data  = jsn )    # We add record with key == 'spider'
        r = requests.post(url, data  = jsn )    # Trying to add one more time
        self.assertEqual(str(r), '<Response [409]>')

        url = 'http://localhost:8000/kv/robber/'  # deleting 'robber' record
        requests.delete(url)                      #


class TestPUTMethod(unittest.TestCase):

    def test_PUT_OK(self):
        url = 'http://localhost:8000/kv/'         # We add record with key == 'six_eyed'
        requestData = {"key" : "six_eyed", "value" : {"mail": "ru", "group" : "company"}}
        jsn = json.dumps(requestData)
        r = requests.post(url, data  = jsn )

        url = 'http://localhost:8000/kv/six_eyed/'
        requestData = {"value" : {"men": "2", "women" : "4"}}
        jsn = json.dumps(requestData)
        r = requests.put(url, data  = jsn )
        self.assertEqual(str(r), '<Response [200]>')

        url = 'http://localhost:8000/kv/six_eyed/'  # deleting 'six_eyed' record
        requests.delete(url)                        #

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
        url = 'http://localhost:8000/kv/'         # We add record with key == 'vagrant'
        requestData = {"key" : "vagrant", "value" : {"mail": "ru", "group" : "company"}}
        jsn = json.dumps(requestData)
        r = requests.post(url, data  = jsn )

        url = 'http://localhost:8000/kv/vagrant/'
        r = requests.get(url)
        self.assertEqual(str(r), '<Response [200]>')

        url = 'http://localhost:8000/kv/vagrant/'   # deleting 'vargant' record
        requests.delete(url)                        #

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
        url = 'http://localhost:8000/kv/'         # We add record with key == 'pouch'
        requestData = {"key" : "pouch", "value" : {"mail": "ru", "group" : "company"}}
        jsn = json.dumps(requestData)
        r = requests.post(url, data  = jsn )

        url = 'http://localhost:8000/kv/pouch/'
        r = requests.delete(url)
        self.assertEqual(str(r), '<Response [200]>')



if __name__ == '__main__':
    unittest.main()
