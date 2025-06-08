import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import unittest
from src.q07_calendar_module.util import get_day_name
class TestQ7(unittest.TestCase):

    def test_valid_dates(self):
        self.assertEqual(get_day_name(8, 5, 2015), 'WEDNESDAY')  # 08 → 8, 05 → 5
        self.assertEqual(get_day_name(1, 1, 2000), 'SATURDAY')
        self.assertEqual(get_day_name(12, 25, 2022), 'SUNDAY')

    def test_leap_year(self):
        self.assertEqual(get_day_name(2, 29, 2020), 'SATURDAY')

if __name__ == '__main__':
    unittest.main()