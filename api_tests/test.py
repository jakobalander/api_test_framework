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
        cls.data = json.loads(response.read())

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_correct_full_repo_name(self):
        thisRepo = None
        for entry in self.data:
            if entry["name"] == "api_test_framework":
                thisRepo = entry
                break
        self.assertEquals(entry["full_name"], "jakobadlander/api_test_framework")
