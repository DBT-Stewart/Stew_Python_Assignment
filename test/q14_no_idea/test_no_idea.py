import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import unittest
from src.q14_no_idea.util import calculate_happiness

class TestQ14(unittest.TestCase):

    def test_case_1(self):
        arr = [1, 5, 3]
        A = {3, 1}
        B = {5, 7}
        self.assertEqual(calculate_happiness(arr, A, B), 1) # +1 (1) +1 (3) -1 (5)

    def test_case_2(self):
        arr = [1, 2, 3, 4]
        A = {1, 3}
        B = {2, 4}
        self.assertEqual(calculate_happiness(arr, A, B), 0)  # +1 +1 -1 -1

    def test_case_3(self):
        arr = [1, 2, 2, 3, 3, 4]
        A = {2, 3}
        B = {1}
        self.assertEqual(calculate_happiness(arr, A, B), 3)  # -1 +1 +1 +1 +1 +0 = 3

if __name__ == '__main__':
    unittest.main()
