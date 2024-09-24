from books import load_books, add_book, borrow_book, return_book, display_books, search_books, generate_available_books_report, generate_borrowed_books_report
from borrowers import load_borrowers, display_borrowers
from utils import valid_input

def main():
    load_books()
    load_borrowers()

    while True:
        print("\n1. Add a Book")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Display Books")
        print("5. Search Books")
        print("6. Display Borrowers")
        print("7. Generate Available Books Report")  # توليد تقرير الكتب المتاحة
        print("8. Generate Borrowed Books Report")  # توليد تقرير الكتب المستعارة
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = valid_input("Enter the book title: ")
            author = valid_input("Enter the author's name: ")
            add_book(title, author)
        elif choice == '2':
            title = valid_input("Enter the book title to borrow: ")
            borrow_book(title)
        elif choice == '3':
            title = valid_input("Enter the book title to return: ")
            return_book(title)
        elif choice == '4':
            display_books()
        elif choice == '5':
            query = valid_input("Enter book title or author to search: ")
            search_books(query)
        elif choice == '6':
            display_borrowers()
        elif choice == '7':
            generate_available_books_report()
        elif choice == '8':
            generate_borrowed_books_report()
        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
