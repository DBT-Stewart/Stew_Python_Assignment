import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import unittest
from src.q10_min_and_max.util import max_of_row_minimums

class TestQ10(unittest.TestCase):

    def test_max_of_min(self):
        matrix = [
            [3, 7, 2],
            [1, 9, 5],
            [8, 4, 6]
        ]
        # Row minimums: [2, 1, 4] → max is 4
        self.assertEqual(max_of_row_minimums(matrix), 4)

    def test_single_row(self):
        matrix = [[5, 3, 9]]
        # Min is 3 → max is 3
        self.assertEqual(max_of_row_minimums(matrix), 3)

    def test_single_column(self):
        matrix = [[5], [2], [7]]
        # Row minimums = each value → max is 7
        self.assertEqual(max_of_row_minimums(matrix), 7)

if __name__ == '__main__':
    unittest.main()
