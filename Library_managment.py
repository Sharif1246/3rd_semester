
from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, name, email):
        self.name = name
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email address")
        self._email = value

    @abstractmethod
    def role_info(self):
        pass


class Member(Person):

    def __init__(self, name, email, member_id):
        super().__init__(name, email)
        self.member_id = member_id

    def role_info(self):
        return "Library Member"

    def __str__(self):
        return f"Member: {self.name}, ID: {self.member_id}"

    def __repr__(self):
        return f"Member('{self.name}', '{self.email}', '{self.member_id}')"


class Librarian(Person):

    def __init__(self, name, email, employee_id):
        super().__init__(name, email)
        self.employee_id = employee_id

    def role_info(self):
        return "Librarian"

    def __str__(self):
        return f"Librarian: {self.name}, Employee ID: {self.employee_id}"

    def __repr__(self):
        return f"Librarian('{self.name}', '{self.email}', '{self.employee_id}')"


class Book:

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} - {status}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.isbn}')"


class Loan:

    def __init__(self, book, member, loan_date):
        self.book = book
        self.member = member
        self.loan_date = loan_date
        self.returned = False

    def return_book(self):
        self.returned = True
        self.book.available = True

    def __str__(self):
        status = "Returned" if self.returned else "Not Returned"
        return f"{self.book.title} borrowed by {self.member.name} - {status}"

    def __repr__(self):
        return f"Loan({self.book!r}, {self.member!r}, '{self.loan_date}')"


class Library:

    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []
        self.loans = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, book, member, loan_date):
        if book not in self.books:
            print("Book is not in the library.")
            return

        if member not in self.members:
            print("Member is not registered.")
            return

        if not book.available:
            print("Book is already borrowed.")
            return

        loan = Loan(book, member, loan_date)
        self.loans.append(loan)
        book.available = False

        print(f"{member.name} borrowed '{book.title}'.")

    def return_book(self, book):
        for loan in self.loans:
            if loan.book == book and not loan.returned:
                loan.return_book()
                print(f"'{book.title}' has been returned.")
                return

        print("No active loan found for this book.")

    def show_books(self):
        print("\nBooks in Library:")
        for book in self.books:
            print(book)

    def show_members(self):
        print("\nLibrary Members:")
        for member in self.members:
            print(member)

    def show_loans(self):
        print("\nLoans:")
        for loan in self.loans:
            print(loan)

    def __str__(self):
        return (
            f"Library: {self.name}\n"
            f"Books: {len(self.books)}\n"
            f"Members: {len(self.members)}\n"
            f"Loans: {len(self.loans)}"
        )


# Creating objects

member1 = Member("Ahmad", "ahmad@gmail.com", "M001")
member2 = Member("Ali", "ali@gmail.com", "M002")

librarian1 = Librarian("Dr. Rahimi", "rahimi@gmail.com", "L001")

book1 = Book("Python Programming", "John Smith", "ISBN001")
book2 = Book("Artificial Intelligence", "Andrew Ng", "ISBN002")
book3 = Book("Computer Networks", "James Kurose", "ISBN003")


# Creating library

library = Library("Kabul Central Library")


# Adding books and members

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.add_member(member1)
library.add_member(member2)


# Polymorphism

people = [member1, member2, librarian1]

print("Roles:")
for person in people:
    print(person.name, ":", person.role_info())


# Display information

print("\nLibrary Information:")
print(library)

library.show_books()
library.show_members()


# Borrowing books

print("\nBorrowing Books:")

library.borrow_book(book1, member1, "2026-09-17")
library.borrow_book(book2, member2, "2026-09-17")


# Display loans

library.show_loans()

# Return a book

print("\nReturning Book:")
library.return_book(book1)

# Display books again

library.show_books()
