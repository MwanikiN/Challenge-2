import unittest

from statistics import list_statistics

 
class TestStatistics(unittest.TestCase):
    def test_statistics(self):
        self.assertEqual(14.5, list_statistics([58,6,9,7,2,5]))

if __name__ =="__main__":
    unittest.main()