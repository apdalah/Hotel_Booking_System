import os

BORROWERS_FILE = "data/borrowers.txt"
borrowers = []

# Load borrowers from file
def load_borrowers():
    if os.path.exists(BORROWERS_FILE):
        with open(BORROWERS_FILE, "r") as file:
            for line in file:
                title, borrower = line.strip().split(" - ")
                borrowers.append({'title': title, 'borrower': borrower})

# Save borrowers to file
def save_borrowers():
    with open(BORROWERS_FILE, "w") as file:
        for entry in borrowers:
            file.write(f"{entry['title']} - {entry['borrower']}\n")

# Display all borrowers
def display_borrowers():
    if borrowers:
        print("Current borrowers:")
        for entry in borrowers:
            print(f"{entry['borrower']} borrowed '{entry['title']}'")
    else:
        print("No books are currently borrowed.")
