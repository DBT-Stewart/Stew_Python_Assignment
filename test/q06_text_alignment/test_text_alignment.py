import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.q06_text_alignment.util import generate_h_logo
class TestQ6(unittest.TestCase):
    def test_valid_output_small(self):
        result = generate_h_logo(3)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3 + 4 + 2 + 4 + 3)  # Top cone + top pillars + belt + bottom pillars + cone

    def test_even_thickness(self):
        with self.assertRaises(ValueError):
            generate_h_logo(4)

    def test_output_sample_content(self):
        result = generate_h_logo(3)
        self.assertTrue(any('H' in line for line in result))

if __name__ == '__main__':
    unittest.main()
