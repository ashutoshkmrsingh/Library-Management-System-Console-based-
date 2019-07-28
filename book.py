"""
    Book module contains BookClass and book_list data structure.

    BookClass used to create book objects.

    And, book_list is a list data structure which stores the book objects,
    and used for modifying book data and storing it in a pickle file named as "book_data.pkl"
"""


class BookClass:
    """
        The BookClass contains information of the books available in library.

        BookClass have following attributes:
            1. title = Contains title of the book.
            2. author = Contains author name of the book.
            3. isbn = Contains isbn number of the book.
            4. num_copies = Contains number of copies available in library.
    """
    def __init__(self, title=None, author=None, isbn=None, num_of_copies=None):
        """Initialises BookClass object variables with given arguments. Default arguments are None"""
        self.title, self.author, self.isbn, self.num_of_copies = title, author, isbn, num_of_copies

    def set(self, title=None, author=None, isbn=None, num_of_copies=None):
        """Set or modify BookClass object variables with given arguments. Default arguments are None"""
        self.title, self.author, self.isbn, self.num_of_copies = title, author, isbn, num_of_copies

    def __str__(self):
        return f'Book Title is {self.title}, Author is {self.author}, ISBN is {self.isbn} ' \
               f'and number of copies are {self.num_of_copies}'\



book_list = []