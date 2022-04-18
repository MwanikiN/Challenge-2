import unittest
from request_timeout import timeout_request

class TestRequestTimeout (unittest.TestCase):
    def test_request_timeout(self):
        self.assertEqual(200, timeout_request("https://api.github.com", 3))
        self.assertEqual("Timeout exceeded", timeout_request("https://api.github.com", 0.001))
        

if __name__ == "__main__":
    unittest.main()