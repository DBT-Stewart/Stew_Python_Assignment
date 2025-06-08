import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import unittest
import numpy as np
from src.q12_mean_var_std.util import calculate_stats

class TestQ12(unittest.TestCase):

    def test_stats_1(self):
        matrix = [
            [1, 2],
            [3, 4]
        ]
        mean, var, std_dev = calculate_stats(matrix)
        np.testing.assert_array_almost_equal(mean, [1.5, 3.5])
        np.testing.assert_array_almost_equal(var, [1.0, 1.0])
        self.assertAlmostEqual(std_dev, 1.11803398875, places=11)

    def test_stats_2(self):
        matrix = [
            [10, 20],
            [30, 40],
            [50, 60]
        ]
        mean, var, std_dev = calculate_stats(matrix)
        np.testing.assert_array_almost_equal(mean, [15, 35, 55])
        np.testing.assert_array_almost_equal(var, [266.66666667, 266.66666667])
        self.assertAlmostEqual(std_dev, 17.0782512766, places=11)

if __name__ == '__main__':
    unittest.main()
