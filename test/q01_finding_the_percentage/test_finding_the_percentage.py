import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.q01_finding_the_percentage.util import s_mark

class TestQ1(unittest.TestCase):
    def test_valid_student(self):
        data = {
            "Alice": [50, 60, 70],
            "Bob": [90, 80, 70]
        }
        self.assertEqual(s_mark(data, "Bob"), 80.0)

    def test_invalid_student(self):
        data = {
            "Alice": [50, 60, 70]
        }
        self.assertIsNone(s_mark(data, "Charlie"))

    def test_precision(self):
        data = {
            "David": [33.33, 66.66, 99.99]
        }
        self.assertEqual(s_mark(data, "David"), 66.66)

if __name__ == '__main__':
    unittest.main()
