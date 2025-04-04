""" """ """ #develop a library management system in python that allows users to manage books ,issue books to members the system must create class 1) for books  members with librarians with appropriate attributes with method
2) implement operater overloading to facilitate book transaction dynamically 
3) use inheritence and super keyword to extend the functionalities of different user roles 
4) demonstrate method over riding and polymorphism to customoze user action 
5) apply encapsulation by making sensitive data private and access it via getter method """

""" first we will make a class including a empty distionary and add elements in the dictonary according to it,  
then we will make a class for book and member and librarian with their attributes and methods 
then we will implement operator overloading to facilitate book transaction dynamically, 
then we will use inheritance and super keyword to extend the functionalities of different user roles, 
then we will demonstrate method over riding and polymorphism to customize user action,
then we will apply encapsulation by making sensitive data private and access it via getter method """ """

import datetime

class Person:
    def __init__(self, name, person_id):
        self.__name = name
        self.__person_id = person_id

    def get_id(self):
        return self.__person_id

    def display_info(self):
        print(f"Name: {self.__name}, ID: {self.__person_id}")


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
        self.borrowed_id = None
        self.due_date = None

    def __str__(self):
        status = "Available" if self.is_available else f"Borrowed by {self.borrowed_id}"
        due = f"Due date: {self.due_date.strftime('%Y-%m-%d')}" if self.due_date else "Not borrowed"
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {status}, {due}"

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.isbn})"


class Member(Person):
    def __init__(self, name, member_id):
        super().__init__(name, member_id)
        self.__borrowed_books = {}

    def borrow_book(self, book):
        if isinstance(book, Book) and book.is_available:
            book.is_available = False
            book.borrowed_id = self.get_id()
            book.due_date = datetime.datetime.now() + datetime.timedelta(days=14)
            self.__borrowed_books[book.isbn] = book
            print(f"Book '{book.title}' borrowed successfully.")
        else:
            print("Book is not available for borrowing.")

    def return_book(self, book):
        if isinstance(book, Book) and book.isbn in self.__borrowed_books:
            book.is_available = True
            book.borrowed_id = None
            book.due_date = None
            del self.__borrowed_books[book.isbn]
            print(f"Book '{book.title}' returned successfully.")
        else:
            print("This book was not borrowed by the member.")

    def display_info(self):
        super().display_info()
        print(", Role: Member")
        borrowed_count = len(self.__borrowed_books)
        if borrowed_count > 0:
            print(f"Borrowed books ({borrowed_count}):")
            for isbn, book in self.__borrowed_books.items():
                print(f"  - {book.title} (ISBN: {isbn}), Due: {book.due_date.strftime('%Y-%m-%d')}")
        else:
            print("No borrowed books.")
        print("-" * 20)

    def __str__(self):
        return f"Member: {self._Person__name}, ID: {self._Person__person_id}"

    def __repr__(self):
        return f"Member({self._Person__name}, {self._Person__person_id})"


class Librarian(Person):
    def __init__(self, name, librarian_id):
        super().__init__(name, librarian_id)
        self.__managed_books = {}

    def add_book(self, book):
        if isinstance(book, Book):
            self.__managed_books[book.isbn] = book
            print(f"Book '{book.title}' added to the library.")
        else:
            print("Invalid book object.")

    def remove_book(self, book):
        if isinstance(book, Book) and book.isbn in self.__managed_books:
            del self.__managed_books[book.isbn]
            print(f"Book '{book.title}' removed from the library.")
        else:
            print("Book not found in the library.")

    def display_info(self):
        super().display_info()
        print(", Role: Librarian")
        managed_count = len(self.__managed_books)
        if managed_count > 0:
            print(f"Managed books ({managed_count}):")
            for isbn, book in self.__managed_books.items():
                print(f"  - {book.title} (ISBN: {isbn})")
        else:
            print("No managed books.")
        print("-" * 20)

    def __str__(self):
        return f"Librarian: {self._Person__name}, ID: {self._Person__person_id}"

    def __repr__(self):
        return f"Librarian({self._Person__name}, {self._Person__person_id})"


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.librarians = {}

    def add_book(self, book):
        if isinstance(book, Book):
            self.books[book.isbn] = book
            print(f"Book '{book.title}' added to the library collection.")
        else:
            print("Invalid book object.")

    def add_member(self, member):
        if isinstance(member, Member):
            self.members[member.get_id()] = member
            print(f"Member '{member._Person__name}' added to the library.")
        else:
            print("Invalid member object.")

    def add_librarian(self, librarian):
        if isinstance(librarian, Librarian):
            self.librarians[librarian.get_id()] = librarian
            print(f"Librarian '{librarian._Person__name}' added to the library.")
        else:
            print("Invalid librarian object.")

    def display_books(self):
        if self.books:
            print("Library Books:")
            for isbn, book in self.books.items():
                print(f"  - {book}")
        else:
            print("No books in the library.")

    def display_members(self):
        if self.members:
            print("Library Members:")
            for member_id, member in self.members.items():
                print(f"  - {member}")
        else:
            print("No members in the library.")

    def display_librarians(self):
        if self.librarians:
            print("Library Librarians:")
            for librarian_id, librarian in self.librarians.items():
                print(f"  - {librarian}")
        else:
            print("No librarians in the library.") """


import datetime
import sys # To exit the program

# --- Core Classes (Mostly Unchanged from Experiment 3) ---

# Base Class for Users
class User:
    def __init__(self, name, user_id):
        self._name = name
        self._user_id = user_id

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def display_info(self):
        print(f"  User ID: {self._user_id}, Name: {self._name}")

# Book Class
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self._isbn = isbn
        self._is_available = True

    def get_isbn(self):
        return self._isbn

    def is_available(self):
        return self._is_available

    def borrow(self):
        if self._is_available:
            self._is_available = False
            return True
        return False

    def return_book(self):
        if not self._is_available:
            self._is_available = True
            return True
        return False

    def __str__(self):
        status = "Available" if self._is_available else "Borrowed"
        return f"'{self.title}' by {self.author} (ISBN: {self._isbn}) - {status}"

# Member Class (Inherits from User)
class Member(User):
    def __init__(self, name, user_id):
        super().__init__(name, user_id)
        self._borrowed_books = []

    def get_borrowed_books(self):
        return list(self._borrowed_books)

    # Operator Overloading for book transactions
    def __iadd__(self, book):
        if isinstance(book, Book):
            # Ensure book isn't already borrowed by this member *before* calling borrow()
            if book in self._borrowed_books:
                print(f"! Member {self.get_name()} already has '{book.title}' borrowed.")
                return self # Return self without changes

            if book.borrow(): # Check availability and mark as borrowed
                self._borrowed_books.append(book)
                print(f"+ Member {self.get_name()} borrowed '{book.title}'")
            else:
                print(f"! '{book.title}' is currently unavailable.")
        else:
            print("! Invalid item to add. Must be a Book object.")
        return self

    def __isub__(self, book):
        if isinstance(book, Book):
            if book in self._borrowed_books:
                if book.return_book(): # Mark as available
                    self._borrowed_books.remove(book)
                    print(f"- Member {self.get_name()} returned '{book.title}'")
                else:
                    print(f"! Error processing return for '{book.title}'.")
            else:
                print(f"! '{book.title}' was not borrowed by Member {self.get_name()}.")
        else:
            print("! Invalid item to remove. Must be a Book object.")
        return self

    # Method Overriding
    def display_info(self):
        super().display_info()
        print("  Role: Member")
        if self._borrowed_books:
            print("  Borrowed Books:")
            for book in self._borrowed_books:
                print(f"    - {book.title} (ISBN: {book.get_isbn()})")
        else:
            print("  No books currently borrowed.")

# Librarian Class (Inherits from User)
class Librarian(User):
    def __init__(self, name, user_id, employee_id):
        super().__init__(name, user_id)
        self._employee_id = employee_id

    def get_employee_id(self):
        return self._employee_id

    # Method Overriding
    def display_info(self):
        super().display_info()
        print("  Role: Librarian")
        print(f"  Employee ID: {self._employee_id}")

    # Librarian-specific actions now use the member's overloaded operators
    def issue_book(self, member, book):
        print(f"\n> Librarian {self.get_name()} attempting to issue '{book.title}' to {member.get_name()}...")
        member += book # Utilize overloaded += on member

    def receive_book(self, member, book):
        print(f"\n> Librarian {self.get_name()} attempting to receive '{book.title}' from {member.get_name()}...")
        member -= book # Utilize overloaded -= on member

# --- Dynamic Interaction Logic ---

# Data Storage (simple dictionaries for this example)
books_catalog = {} # key: isbn, value: Book object
members = {}       # key: user_id, value: Member object
librarians = {}    # key: user_id, value: Librarian object

def add_new_book():
    """Prompts user for book details and adds it to the catalog."""
    print("\n--- Add New Book ---")
    try:
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        isbn = input("Enter book ISBN: ")
        if not title or not author or not isbn:
            print("! Book title, author, and ISBN cannot be empty.")
            return
        if isbn in books_catalog:
            print(f"! Book with ISBN {isbn} already exists.")
            return
        book = Book(title, author, isbn)
        books_catalog[isbn] = book
        print(f"Book '{title}' added successfully.")
    except Exception as e:
        print(f"! Error adding book: {e}")

def add_new_member():
    """Prompts user for member details and adds them."""
    print("\n--- Add New Member ---")
    try:
        name = input("Enter member name: ")
        user_id = input("Enter member ID (e.g., M001): ")
        if not name or not user_id:
            print("! Member name and ID cannot be empty.")
            return
        if user_id in members or user_id in librarians:
            print(f"! User ID {user_id} already exists.")
            return
        member = Member(name, user_id)
        members[user_id] = member
        print(f"Member '{name}' added successfully.")
    except Exception as e:
        print(f"! Error adding member: {e}")

def add_librarian():
    """Adds a librarian (can be simplified or expanded)."""
    print("\n--- Add New Librarian ---")
    try:
        name = input("Enter librarian name: ")
        user_id = input("Enter librarian user ID (e.g., L001): ")
        emp_id = input("Enter librarian employee ID: ")
        if not name or not user_id or not emp_id:
            print("! Librarian name, user ID, and employee ID cannot be empty.")
            return
        if user_id in members or user_id in librarians:
            print(f"! User ID {user_id} already exists.")
            return
        librarian = Librarian(name, user_id, emp_id)
        librarians[user_id] = librarian
        print(f"Librarian '{name}' added successfully.")
    except Exception as e:
        print(f"! Error adding librarian: {e}")


def list_all_books():
    print("\n--- Library Catalog ---")
    if not books_catalog:
        print("The library catalog is empty.")
        return
    for isbn, book in books_catalog.items():
        print(book) # Uses the __str__ method of the Book class
    print("-" * 20)

def list_all_members():
    print("\n--- Library Members ---")
    if not members:
        print("There are no registered members.")
        return
    for user_id, member in members.items():
        print(f"ID: {user_id}, Name: {member.get_name()}") # Use getter
    print("-" * 20)

def list_all_librarians():
    print("\n--- Library Librarians ---")
    if not librarians:
        print("There are no registered librarians.")
        return
    for user_id, librarian in librarians.items():
        print(f"ID: {user_id}, Name: {librarian.get_name()}, EmpID: {librarian.get_employee_id()}") # Use getters
    print("-" * 20)


def handle_issue_book():
    print("\n--- Issue Book ---")
    if not librarians:
        print("! No librarians available to issue books.")
        return
    librarian_id = input("Enter Librarian User ID performing the action: ")
    member_id = input("Enter Member User ID to issue to: ")
    isbn = input("Enter ISBN of the book to issue: ")

    librarian = librarians.get(librarian_id)
    member = members.get(member_id)
    book = books_catalog.get(isbn)

    if not librarian:
        print(f"! Librarian with ID {librarian_id} not found.")
        return
    if not member:
        print(f"! Member with ID {member_id} not found.")
        return
    if not book:
        print(f"! Book with ISBN {isbn} not found.")
        return

    # Librarian performs the action using the method
    librarian.issue_book(member, book)


def handle_return_book():
    print("\n--- Return Book ---")
    if not librarians:
        print("! No librarians available to receive books.")
        return
    librarian_id = input("Enter Librarian User ID performing the action: ")
    member_id = input("Enter Member User ID returning the book: ")
    isbn = input("Enter ISBN of the book to return: ")

    librarian = librarians.get(librarian_id)
    member = members.get(member_id)
    book = books_catalog.get(isbn) # Need the book object even if it's borrowed

    if not librarian:
        print(f"! Librarian with ID {librarian_id} not found.")
        return
    if not member:
        print(f"! Member with ID {member_id} not found.")
        return
    if not book:
         # Check if it exists in the catalog at all, even if not found directly by ISBN maybe?
         # For simplicity, we assume ISBN lookup is sufficient.
         # A more robust system might search within member's borrowed list if catalog lookup fails.
        print(f"! Book with ISBN {isbn} not found in catalog.")
        return

    # Librarian performs the action using the method
    librarian.receive_book(member, book)


def display_user_details():
    print("\n--- Display User Details ---")
    user_id = input("Enter User ID (Member or Librarian): ")
    user = members.get(user_id) or librarians.get(user_id)

    if user:
        user.display_info() # Polymorphism in action!
    else:
        print(f"! User with ID {user_id} not found.")

def display_menu():
    print("\n===== Library Management System =====")
    print("1. Add New Book")
    print("2. Add New Member")
    print("3. Add New Librarian")
    print("4. List All Books")
    print("5. List All Members")
    print("6. List All Librarians")
    print("7. Issue Book to Member")
    print("8. Return Book from Member")
    print("9. Display User Details (Member/Librarian)")
    print("0. Exit")
    print("=====================================")

# --- Main Execution ---
def main():
    # Add a default librarian to start
    if not librarians:
         librarians["L001"] = Librarian("Admin Librarian", "L001", "EMP001")
         print("Default Librarian (L001) created.")

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_new_book()
        elif choice == '2':
            add_new_member()
        elif choice == '3':
            add_librarian()
        elif choice == '4':
            list_all_books()
        elif choice == '5':
            list_all_members()
        elif choice == '6':
            list_all_librarians()
        elif choice == '7':
            handle_issue_book()
        elif choice == '8':
            handle_return_book()
        elif choice == '9':
            display_user_details()
        elif choice == '0':
            print("Exiting Library Management System. Goodbye!")
            sys.exit() # Exit the program
        else:
            print("! Invalid choice. Please try again.")
        input("\nPress Enter to continue...") # Pause screen

if __name__ == "__main__":
    main()