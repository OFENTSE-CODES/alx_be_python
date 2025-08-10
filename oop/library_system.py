class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"


# Derived class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Call the base class constructor
        self.file_size = file_size  # in MB

    def __str__(self):
        return f"{super().__str__()} [EBook, {self.file_size}MB]"


# Derived class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Call the base class constructor
        self.page_count = page_count  # number of pages

    def __str__(self):
        return f"{super().__str__()} [PrintBook, {self.page_count} pages]"


# Composition - Library
class Library:
    def __init__(self):
        self.books = []  # list to store Book objects

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only instances of Book, EBook, or PrintBook can be added.")

    def list_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f"- {book}")