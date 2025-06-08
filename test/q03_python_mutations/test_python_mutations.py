import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.q03_python_mutations.util import mutate_string

class TestQ3(unittest.TestCase):
    def test_basic_mutation(self):
        self.assertEqual(mutate_string("hello", 1, "a"), "hallo")

    def test_end_position(self):
        self.assertEqual(mutate_string("world", 4, "Z"), "worlZ")

    def test_start_position(self):
        self.assertEqual(mutate_string("apple", 0, "A"), "Apple")

    def test_invalid_position(self):
        with self.assertRaises(IndexError):
            mutate_string("data", 5, "x")

if __name__ == '__main__':
    unittest.main()
