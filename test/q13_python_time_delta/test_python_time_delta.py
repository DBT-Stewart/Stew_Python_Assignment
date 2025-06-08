import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.q13_python_time_delta.util import time_delta

class TestQ13(unittest.TestCase):

    def test_example_case_1(self):
        t1 = "Sun 10 May 2015 13:54:36 -0700"
        t2 = "Sun 10 May 2015 13:54:36 -0000"
        self.assertEqual(time_delta(t1, t2), "25200")  # 7 hours * 3600

    def test_example_case_2(self):
        t1 = "Sat 02 May 2015 19:54:36 +0530"
        t2 = "Fri 01 May 2015 13:54:36 -0000"
        self.assertEqual(time_delta(t1, t2), "88200")

    def test_same_time(self):
        t = "Sun 10 May 2015 13:54:36 +0000"
        self.assertEqual(time_delta(t, t), "0")

if __name__ == '__main__':
    unittest.main()
