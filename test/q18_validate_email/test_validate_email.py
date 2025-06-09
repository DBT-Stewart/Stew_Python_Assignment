import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from unittest.mock import patch
from src.q18_validate_email.util import is_valid_email, filter_emails


class TestEmailValidation(unittest.TestCase):
    def test_valid_email(self):
        # Test a valid email address
        self.assertTrue(is_valid_email("example@email.com"))
    def test_invalid_email(self):
        # Test an invalid email address
        self.assertFalse(is_valid_email("invalid.email.com"))



if __name__ == '__main__':
    unittest.main()