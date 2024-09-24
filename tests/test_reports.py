import unittest
import os
from books import generate_available_books_report, generate_borrowed_books_report, books
from borrowers import borrowers, save_borrowers
import sys

# إضافة مسار فولدر code لاستيراد الدوال
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../code')))

# تعديل المسار ليطابق مكان فولدر output
OUTPUT_FOLDER = "../output"


class TestReports(unittest.TestCase):

    def setUp(self):
        """Setup the environment before each test."""
        books.clear()
        borrowers.clear()

        # Ensure the output folder exists
        if not os.path.exists(OUTPUT_FOLDER):
            os.makedirs(OUTPUT_FOLDER)

        # Remove old report files if they exist
        available_report = os.path.join(OUTPUT_FOLDER, "available_books_report.txt")
        borrowed_report = os.path.join(OUTPUT_FOLDER, "borrowed_books_report.txt")

        if os.path.exists(available_report):
            os.remove(available_report)
        if os.path.exists(borrowed_report):
            os.remove(borrowed_report)

    def test_generate_available_books_report(self):
        """Test generating the available books report."""
        books.append({"title": "1984", "author": "George Orwell", "available": True})
        generate_available_books_report()
        report_file = os.path.join(OUTPUT_FOLDER, "available_books_report.txt")

        # Check if the report file is created
        self.assertTrue(os.path.exists(report_file))

        # Check content of the file
        with open(report_file, "r") as file:
            content = file.read()
            self.assertIn("1984 by George Orwell", content)

    def test_generate_borrowed_books_report(self):
        """Test generating the borrowed books report."""
        books.append({"title": "The Catcher in the Rye", "author": "J.D. Salinger", "available": False})
        borrowers.append({"title": "The Catcher in the Rye", "borrower": "Alice Johnson"})
        save_borrowers()
        generate_borrowed_books_report()
        report_file = os.path.join(OUTPUT_FOLDER, "borrowed_books_report.txt")

        # Check if the report file is created
        self.assertTrue(os.path.exists(report_file))

        # Check content of the file
        with open(report_file, "r") as file:
            content = file.read()
            self.assertIn("The Catcher in the Rye - Borrowed by Alice Johnson", content)


if __name__ == "__main__":
    unittest.main()
