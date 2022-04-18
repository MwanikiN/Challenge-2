import unittest
from powers_4 import powers_of_four

class TestPower(unittest.TestCase):
  def test_power_num(self):
    
    self.assertEqual(256, powers_of_four(4), "You raised an error")

if __name__ == "__main__":
    unittest.main()
