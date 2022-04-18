import unittest
from public_data import public_data

class TestPublicData (unittest.TestCase):
    def test_public_data(self):
        self.assertIsInstance("https://api.github.com", public_data("https://api.google.com"))
        

if __name__ == "__main__":
    unittest.main()