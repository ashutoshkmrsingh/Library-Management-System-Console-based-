# Create a class StudentClass which contain following attributes name year_of_admn
# Branch, admn_id_no , roll_no(yearofadmission+0187+branch+admission_id)
# ,num_books_issued, book_issued
"""
    Student module contains StudentClass and student_data_list data structure.

    StudentClass used to create student objects.

    And, student_data_list is a list data structure which stores the student objects,
    and used for modifying student data and storing it in a pickle file named as "student_data.pkl"
"""


class StudentClass:
    """
        The StudentClass contains information of the Student.

        StudentClass have following attributes:
            1. name = Contains name of the student.
            2. year_of_admn = Contains id of the student.
            3. branch = Contains branch of the student.
            3. admn_id_no = Contains admission id number of the student.
            3. roll_no = Contains roll number of the student.
            3. b_i = A list data structure, stores book objects issued to the student.
            3. b_i_d = A list data structure, stores book objects issued to the faculty.
    """
    def __init__(self, name=None, year_of_admn=None, branch=None, admn_id_no=None, roll_no=None, b_i=[], b_i_d=[]):
        """Initialises BookClass object variables with given arguments. Default arguments are None"""
        self.name, self.year_of_admn, self.branch, self.admn_id_no = name, year_of_admn, branch, admn_id_no
        self.roll_no, self.book_issued, self.book_issued_details = roll_no, b_i, b_i_d

    def set(self, name=None, year_of_admn=None, branch=None, admn_id_no=None, roll_no=None, b_i=[], b_i_d=[]):
        """Set or modify StudentClass object variables with given arguments. Default arguments are None"""
        self.name, self.year_of_admn, self.branch, self.admn_id_no = name, year_of_admn, branch, admn_id_no
        self.roll_no, self.book_issued, self.book_issued_details = roll_no, b_i, b_i_d

    def __str__(self):
        return f'Student name is {self.name}, Year of admission is {self.year_of_admn}, ' \
               f'Branch is {self.branch}, Admission Id Number is {self.admn_id_no}, ' \
               f'No. of book issued are {len(self.book_issued)} and Roll number is {self.roll_no},' \
               f'Book issued details are {self.book_issued_details}'

    def book_details(self):
        return self.book_issued_details


student_data_list = []

