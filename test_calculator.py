import unittest
from calculator import add

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 6)   # ❌ intentional bug

if __name__ == '__main__':
    unittest.main()
