"""
    faculty module contains FacultyClass and faculty_list data structure.

    FacultyClass used to create faculty objects.

    And, faculty_list is a list data structure which stores the faculty objects,
    and used for modifying faculty data and storing it in a pickle file named as "faculty_data.pkl"
"""


class FacultyClass:
    """
        The FacultyClass contains information of the faculties.

        FacultyClass have following attributes:
            1. e_name = Contains name of the faculty.
            2. e_id = Contains id of the faculty.
            3. book_issued = A list data structure, stores book objects issued to the faculty.
    """
    def __init__(self, e_name=None, e_id=None, book_issued=[]):
        """Initialises FacultyClass object variables with given arguments. Default arguments are None"""
        self.e_name, self.e_id, self.book_issued = e_name, e_id, book_issued

    def set(self, e_name=None, e_id=None, book_issued=[]):
        """Set or modify FacultyClass object variables with given arguments. Default arguments are None"""
        self.e_name, self.e_id, self.book_issued = e_name, e_id, book_issued

    def __str__(self):
        return f'Faculty name is {self.e_name}, id is {self.e_id} and book issued are {self.book_issued}'


faculty_list = []