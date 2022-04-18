import unittest
from perfect_squares import perfect
class TestPerfect(unittest.TestCase):
    def test_perfect_square(self):
        self.assertEqual(1, perfect(8))

if __name__ =="__main__":
    unittest.main()