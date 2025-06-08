import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import unittest
from src.q04_merge_the_tools.util import merge_the_tools

class TestQ4(unittest.TestCase):
    def test_basic_case(self):
        string = "AABCAAADA"
        k = 3
        expected = ["AB", "CA", "AD"]
        self.assertEqual(merge_the_tools(string, k), expected)

    def test_all_unique(self):
        string = "ABCDE"
        k = 1
        expected = ["A", "B", "C", "D", "E"]
        self.assertEqual(merge_the_tools(string, k), expected)

    def test_all_same(self):
        string = "ZZZZZZ"
        k = 2
        expected = ["Z", "Z", "Z"]
        self.assertEqual(merge_the_tools(string, k), expected)

    def test_mixed_case(self):
        string = "ABABAB"
        k = 2
        expected = ["AB", "AB", "AB"]
        self.assertEqual(merge_the_tools(string, k), expected)

if __name__ == "__main__":
    unittest.main()
