import unittest
from unittest.mock import patch
from utils import valid_input
import sys
import os
# إضافة مسار فولدر code لاستيراد الدوال
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../code')))

class TestValidInput(unittest.TestCase):

    @patch('builtins.input', side_effect=["Valid Input"])
    def test_valid_input(self, mock_input):
        """Test valid input is accepted."""
        result = valid_input("Enter something: ")
        self.assertEqual(result, "Valid Input")

    @patch('builtins.input', side_effect=["", "Valid Input"])
    def test_empty_input(self, mock_input):
        """Test empty input is handled and user is prompted again."""
        result = valid_input("Enter something: ")
        self.assertEqual(result, "Valid Input")

if __name__ == "__main__":
    unittest.main()
