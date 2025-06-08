import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.q02_finding_second_maximum_number.util import sec_large

class TestQ2(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sec_large([2, 3, 6, 6, 5]), 5)

    def test_all_same(self):
        self.assertIsNone(sec_large([4, 4, 4, 4]))

    def test_negative_numbers(self):
        self.assertEqual(sec_large([-2, -3, -1, -5]), -2)

    def test_two_elements(self):
        self.assertEqual(sec_large([10, 20]), 10)

    def test_one_element(self):
        self.assertIsNone(sec_large([5]))

if __name__ == '__main__':
    unittest.main()
