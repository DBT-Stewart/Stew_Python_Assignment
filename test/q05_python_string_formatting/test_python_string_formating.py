import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.q05_python_string_formatting.util import print_formatted

class TestQ5(unittest.TestCase):
    def test_formatting_1(self):
        expected = ["1 1 1 1"]
        self.assertEqual(print_formatted(1), expected)

    def test_formatting_2(self):
        expected = [
            " 1  1  1  1",
            " 2  2  2 10"
        ]
        self.assertEqual(print_formatted(2), expected)

    def test_formatting_4(self):
        expected = [
            "  1   1   1   1",
            "  2   2   2  10",
            "  3   3   3  11",
            "  4   4   4 100"
        ]
        self.assertEqual(print_formatted(4), expected)

    def test_formatting_10(self):
        expected = [
            "   1    1    1    1",
            "   2    2    2   10",
            "   3    3    3   11",
            "   4    4    4  100",
            "   5    5    5  101",
            "   6    6    6  110",
            "   7    7    7  111",
            "   8   10    8 1000",
            "   9   11    9 1001",
            "  10   12    A 1010"
        ]
        self.assertEqual(print_formatted(10), expected)

if __name__ == '__main__':
    unittest.main()