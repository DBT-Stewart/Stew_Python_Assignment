import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import numpy as np
from src.q09_floor_ceil_rint.util import apply_rounding_operations

class TestQ8(unittest.TestCase):

    def test_rounding_operations(self):
        arr = [1.1, 2.5, 3.7, -1.1, -2.5]
        floor_expected = np.array([1., 2., 3., -2., -3.])
        ceil_expected = np.array([2., 3., 4., -1., -2.])
        rint_expected = np.array([1., 2., 4., -1., -2.])

        floor, ceil, rint = apply_rounding_operations(arr)

        np.testing.assert_array_equal(floor, floor_expected)
        np.testing.assert_array_equal(ceil, ceil_expected)
        np.testing.assert_array_equal(rint, rint_expected)

if __name__ == '__main__':
    unittest.main()