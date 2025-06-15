from pickle import FALSE, TRUE


class Book:

    def __init__(self, title, author, _is_checked_out=FALSE):
        self.title = title
        self.author = author
        self._is_checked_out = _is_checked_out


    def check_out_book(self):
        self._is_checked_out = TRUE

    def return_book(self):
        self._is_checked_out = FALSE

        


class Library: 
    def __init__(self, _books=[]):
        self._books = _books

    def add_book(self, book):
        self._books.append(book)
    
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                book.check_out_book()

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book.return_book()

    def list_available_books(self):
        for book in self._books:
            if book._is_checked_out == FALSE:
                print(f"{book.title} by {book.author}")