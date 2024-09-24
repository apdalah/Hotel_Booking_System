import unittest
import sys
import os

# إضافة مسار فولدر code لاستيراد الدوال
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../code')))

from books import add_book, save_books, load_books, books

class TestBooksFunctions(unittest.TestCase):

    def setUp(self):
        """Set up the test environment. Clear books list."""
        books.clear()
        if os.path.exists("../data/test_books.txt"):
            os.remove("../data/test_books.txt")

    def test_add_book(self):
        add_book("1984", "George Orwell")
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]['title'], "1984")
        self.assertTrue(books[0]['available'])

    def test_save_and_load_books(self):
        add_book("1984", "George Orwell")
        save_books()
        books.clear()
        load_books()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]['title'], "1984")

if __name__ == "__main__":
    unittest.main()
