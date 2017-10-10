import httplib
import json
import unittest

class SimpleApiTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        headers = {"User-Agent": "jakobalander"}
        connection = httplib.HTTPSConnection("api.github.com")
        connection.request("GET", "/users/jakobalander/repos", None, headers)
        response = connection.getresponse()
        cls.data = json.dumps(response.read())

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertTrue(True)
