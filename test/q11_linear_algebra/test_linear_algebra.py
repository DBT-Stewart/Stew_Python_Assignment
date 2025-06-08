import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import unittest
from src.q11_linear_algebra.util import calculate_determinant

class TestQ11(unittest.TestCase):

    def test_determinant_2x2(self):
        matrix = [[1, 2], [3, 4]]  # det = -2
        self.assertEqual(calculate_determinant(matrix), -2.0)

    def test_determinant_3x3(self):
        matrix = [[6,1,1],[4,-2,5],[2,8,7]]  # det = -306
        self.assertEqual(calculate_determinant(matrix), -306.0)

    def test_identity_matrix(self):
        matrix = [[1, 0], [0, 1]]  # det = 1
        self.assertEqual(calculate_determinant(matrix), 1.0)

if __name__ == '__main__':
    unittest.main()
