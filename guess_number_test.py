import unittest

from guess_number import guess_number

 
class TestInfinity(unittest.TestCase):
    def test_infinity(self):
        self.assertEqual(9, guess_number(num))

if __name__ =="__main__":
    unittest.main()