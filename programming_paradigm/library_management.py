class Book:
    def __init__(self, title, author):
        self.title = title                    # Public attribute
        self.author = author                  # Public attribute
        self._is_checked_out = False          # Private attribute

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def is_checked_out(self):
        return self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # Private list of Book instances

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_checked_out():
                book.check_out()
                break  # Only check out the first match

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book.is_checked_out():
                book.return_book()
                break  # Only return the first match

    def list_available_books(self):
        for book in self._books:
            if not book.is_checked_out():
                print(f"{book.title} by {book.author}")
