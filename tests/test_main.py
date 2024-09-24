import unittest
import sys
import os
# إضافة مسار فولدر code لاستيراد الدوال
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../code')))

from books import add_book, borrow_book, return_book, books
from borrowers import borrowers
from utils import valid_input  # Import the valid_input function

class TestLibraryManagementSystem(unittest.TestCase):

    def setUp(self):
        """Set up test environment. Clear books and borrowers lists."""
        books.clear()
        borrowers.clear()

    def test_add_book(self):
        add_book("Test Book", "Test Author")
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]['title'], "Test Book")
        self.assertEqual(books[0]['author'], "Test Author")
        self.assertTrue(books[0]['available'])

    def test_borrow_book(self):
        add_book("Test Book", "Test Author")
        borrow_book("Test Book")
        self.assertFalse(books[0]['available'])

    def test_return_book(self):
        add_book("Test Book", "Test Author")
        borrow_book("Test Book")
        return_book("Test Book")
        self.assertTrue(books[0]['available'])

if __name__ == "__main__":
    unittest.main()
