import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import unittest
from src.q08_namedtuple.util import calculate_average_marks

class TestQ9(unittest.TestCase):

    def test_average_marks(self):
        total_students = 3
        columns = ['ID', 'NAME', 'CLASS', 'MARKS']
        data = [
            "1 John 10 87",
            "2 Alice 10 92",
            "3 Bob 10 85"
        ]
        expected_avg = (87 + 92 + 85) / 3
        result = calculate_average_marks(total_students, columns, data)
        self.assertAlmostEqual(result, expected_avg)

if __name__ == '__main__':
    unittest.main()
