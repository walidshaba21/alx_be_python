class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False



class Library:
    def __init__ (self):
        self._books = []

