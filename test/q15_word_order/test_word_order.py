import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.q15_word_order.util import word_order_counter

class TestQ15(unittest.TestCase):

    def test_case_1(self):
        words = ["apple", "banana", "apple", "orange", "banana", "apple"]
        count, values = word_order_counter(words)
        self.assertEqual(count, 3)
        self.assertEqual(values, [3, 2, 1])

    def test_case_2(self):
        words = ["one", "two", "three", "one", "three", "one"]
        count, values = word_order_counter(words)
        self.assertEqual(count, 3)
        self.assertEqual(values, [3, 1, 2])

    def test_case_3(self):
        words = ["test"]
        count, values = word_order_counter(words)
        self.assertEqual(count, 1)
        self.assertEqual(values, [1])

if __name__ == "__main__":
    unittest.main()
