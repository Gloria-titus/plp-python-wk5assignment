class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            return f"You have borrowed '{self.title}'."
        return f"'{self.title}' is currently NOT available."

    def return_book(self):
        self.available = True
        return f"'{self.title}' has been returned."

    def get_details(self):
        return f"{self.title} by {self.author}, {self.year}"


class DigitalBook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size

    def stream(self):
        return f"Streaming {self.title} - Size: {self.file_size}MB"
    def borrow(self):
        return f"{self.title} is a digital book. No need to borrow - stream it anytime."


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            return "No books available in the library."
        return [book.get_details() for book in self.books]

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return f"No book with the title '{title}' found in the library."


library = Library("City Library")
library.add_book(Book("Atomic Habits", "James Clear", 2018))  # Fixed: Use the instance 'library'
library.add_book(DigitalBook("Learn Python", "Guido van Rossum", 2021, 90))  # Fixed: Use the instance 'library'

# List all books
print("Books in the library:")
for book_details in library.list_books():
    print(book_details)

# Find a specific book
book_title = "Atomic Habits"
found_book = library.find_book(book_title)
if isinstance(found_book, Book):
    print(f"Found: {found_book.get_details()}")
else:
    print(found_book)