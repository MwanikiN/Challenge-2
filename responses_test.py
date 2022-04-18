import unittest
from responses import url_requests

class TestResponses (unittest.TestCase):
    def test_responses(self):
        self.assertIn("https://api.google.com", url_requests("https://api.google.com"))

if __name__ == "__main__":
    unittest.main()