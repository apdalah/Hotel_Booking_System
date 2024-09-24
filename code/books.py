import os
from utils import valid_input  # Import the valid_input function
from borrowers import borrowers, save_borrowers  # Import borrowers list and save_borrowers function

BOOKS_FILE = "data/books.txt"
books = []

# Folder for output files
OUTPUT_FOLDER = "../output"

# Load books from file
def load_books():
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "r") as file:
            for line in file:
                title, author, available = line.strip().split(" - ")
                books.append({
                    'title': title,
                    'author': author,
                    'available': available == 'Available'
                })
    else:
        print("Books file not found. A new one will be created.")

# Save books to file
def save_books():
    # Ensure the data folder exists
    if not os.path.exists("data"):
        os.makedirs("data")

    with open(BOOKS_FILE, "w") as file:
        for book in books:
            available = "Available" if book['available'] else "Not Available"
            file.write(f"{book['title']} - {book['author']} - {available}\n")

# Add a new book
def add_book(title, author):
    book = {'title': title, 'author': author, 'available': True}
    books.append(book)
    save_books()
    print(f"Book '{title}' by {author} has been added.")

# Borrow a book
def borrow_book(title):
    for book in books:
        if book['title'] == title and book['available']:
            book['available'] = False
            borrower_name = valid_input("Enter your name: ")
            borrowers.append({'title': title, 'borrower': borrower_name})
            save_books()
            save_borrowers()
            print(f"You have borrowed '{title}'.")
            return
    print(f"Book '{title}' is either not available or already borrowed.")

# Return a borrowed book
def return_book(title):
    for book in books:
        if book['title'] == title and not book['available']:
            book['available'] = True
            save_books()
            print(f"Book '{title}' has been returned.")
            return
    print(f"Book '{title}' is either not borrowed or does not exist.")

# Display all books
def display_books():
    if books:
        print("Books available in the library:")
        for book in books:
            status = 'Available' if book['available'] else 'Not Available'
            print(f"{book['title']} - {book['author']} ({status})")
    else:
        print("The library is currently empty.")

# Search for books by title or author
def search_books(query):
    found_books = [book for book in books if query.lower() in book['title'].lower() or query.lower() in book['author'].lower()]
    if found_books:
        print(f"Books matching '{query}':")
        for book in found_books:
            status = 'Available' if book['available'] else 'Not Available'
            print(f"{book['title']} - {book['author']} ({status})")
    else:
        print(f"No books found matching '{query}'.")




# Ensure output folder exists before saving the report
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

def generate_available_books_report():
    report_file = os.path.join(OUTPUT_FOLDER, "available_books_report.txt")
    with open(report_file, "w") as file:
        file.write("# Available Books Report\n\n")
        available_books = [book for book in books if book['available']]
        for index, book in enumerate(available_books, 1):
            file.write(f"{index}. {book['title']} by {book['author']}\n")
    print(f"Available books report generated: {report_file}")

def generate_borrowed_books_report():
    report_file = os.path.join(OUTPUT_FOLDER, "borrowed_books_report.txt")
    with open(report_file, "w") as file:
        file.write("# Borrowed Books Report\n\n")
        for index, entry in enumerate(borrowers, 1):
            file.write(f"{index}. {entry['title']} - Borrowed by {entry['borrower']}\n")
    print(f"Borrowed books report generated: {report_file}")

