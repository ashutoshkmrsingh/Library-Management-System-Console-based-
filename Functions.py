"""
Function module import BookClass, FacultyClass, StudentsClass and other necessary modules

It contains :
    1. Function to add student in library record.
    2. Function to add faculty in library record..
    3. Function to add book in library record..
    4. Function to issue book to the student.
    5. Function to issue book to the faculty.
    6. Function to return book by the student.
    7. Function to return book by the faculty.
    8. Function to search a book.
    9. Function to print student record.
    10. Function to print faculty record.
    11. Function to print book record.
"""


import datetime
import student
import faculty
import book
import pickle

now = datetime.datetime.now()


def write_branch_roll_mapping_file(key, value):
    """This function takes 'Key' i.e Branch name and 'Value' i.e short name for that branch,
    and add new key value pair to the dictionary and write it in the file."""

    with open('branch_roll_mapping_file.pkl', 'rb') as f:
        branch_roll_mapping_temp = pickle.load(f)
    branch_roll_mapping_temp[key] = value
    with open('branch_roll_mapping_file.pkl','wb') as f:
        pickle.dump(branch_roll_mapping_temp, f)
    print('write complete')


with open('branch_roll_mapping_file.pkl','rb') as f:
    branch_roll_mapping = pickle.load(f)


def load_student_data():
    """This function load data of the student from student_data.pkl file
        to the student_data_list of the student module"""

    with open('student_data.pkl', 'rb') as f:
        student.student_data_list = pickle.load(f)


def dump_student_data():
    """This function store data of the student from student_data_list of the student module
        to the student_data.pkl file"""

    with open('student_data.pkl', 'wb') as f:
        pickle.dump(student.student_data_list, f)


def add_student():
    """
        This function add student in library:
            1) Ask name of student
            2) Ask student year of admission also put constraint year of admission should
                  not be greater than current year otherwise say invalid and try again
            3) Ask admission id it should be 4 digit only otherwise say invalid and try again
            4) Ask student branch
            5) Create std_roll = year_of_admn + '0187' + branch_roll_mapping[branch] + admn_id_no
            6) Check whether student already present or not.
            7) Now creating student using all the details that the user will enter
            8) Add created student to list
            9) Update student student_data.pkl
            10) A student with the same details already exists. Cannot Add Student.
    """
    name = input('Enter Student Name : ')
    year_of_admn = int(input('Enter Year of admission : '))
    if year_of_admn > now.year:
        print('Invalid Year of admission, Try again')
        return
    admn_id_no = input('Enter Admission Id Number ( 4 digit acceptable only) : ')
    if len(admn_id_no) != 4:
        print('Invalid Admission Id, Try again')
        return
    else:
        admn_id_no = int(admn_id_no)
    branch = input('Enter Branch : ')
    try:
        roll_no = str(year_of_admn) + '0187' + branch_roll_mapping[branch] + str(admn_id_no)
    except KeyError:
        print('Invalid Branch')
        return

    load_student_data()

    def check_roll_no(roll):
        """check if student present in library records or not using student roll number."""
        for obj in student.student_data_list:
            if str(obj.roll_no) == roll:
                print('Student with same roll number exists, cannot add you')
                return False
        return True

    if check_roll_no(roll_no):
        student_obj = student.StudentClass(name=name, year_of_admn=year_of_admn, admn_id_no=admn_id_no, roll_no=roll_no, branch=branch)
        student.student_data_list.append(student_obj)
        dump_student_data()
        print(f'Student {name} added to the library')


def load_faculty_data():
    """This function load data of the faculty from faculty_data.pkl file
        to the faculty_list of the faculty module"""

    with open('faculty_data.pkl', 'rb') as f:
        faculty.faculty_list = pickle.load(f)


def dump_faculty_data():
    """This function store data of the student from student_data_list of the student module
        to the student_data.pkl file"""

    with open('faculty_data.pkl', 'wb') as f:
        pickle.dump(faculty.faculty_list, f)


def add_faculty():
    """
        This function add faculty to the library record
            1) Ask faculty name from user
            2) Ask for faculty id until five digit exact id is not given
            3) Check whether faculty is already present or not
            4) create faculty using constructor
            5) add created faculty to list
            6) update faculty_data.pkl file
    """
    name = input('Enter Faculty Name : ')
    faculty_id = input('Enter Faculty Id ( 5 digit only ) : ')
    if len(faculty_id) != 5:
        print('Invalid Faculty Id Id, Try again')
        return
    else:
        faculty_id = int(faculty_id)

    load_faculty_data()

    def check_if_eid_present(faculty_d):
        """This function checks whether faculty already exists in library records or not using faculty id"""
        for obj in faculty.faculty_list:
            if obj.e_id == faculty_d:
                print('Faculty with same Eid exists, cannot add you')
                return False
        return True

    if check_if_eid_present(faculty_id):
        faculty_obj = faculty.FacultyClass(e_name=name, e_id=faculty_id, book_issued=[])
        faculty.faculty_list.append(faculty_obj)
        dump_faculty_data()
        print(f'Faculty {name} is added to the library record')


def load_book_data():
    """This function load data of the book from book_data.pkl file
        to the book_list of the book module"""

    with open('book_data.pkl', 'rb') as f:
        book.book_list = pickle.load(f)


def dump_book_data():
    """This function store data of the student from student_data_list of the student module
        to the student_data.pkl file"""

    with open('book_data.pkl', 'wb') as f:
        pickle.dump(book.book_list, f)


def add_book():
    """
    This function add book to the library record
        1) Ask for parameters of a book from user like title ,author , and isbn and isbn number should be 13 digit only
            if not say invalid data and try again.
        2) Then ask for number of copies of book.
        3) Check the given book with isbn is present.
        4) update the number of copies of book and update the book pikle file record
        5) Then it is new book so update the book list and update the pickle file record

    """
    title = input('Enter Book Title : ')
    author = input('Enter Book Author : ')
    isbn = input('Enter ISBN ( 13 digit only ) : ')
    if len(isbn) != 13:
        print('Invalid ISBN, Try again')
        return
    else:
        isbn = int(isbn)
    no_of_copies = int(input('Enter number of copies : '))
    load_book_data()

    def check_if_isbn_present(isbn):
        """This function checks whether book already exists in library or not using ISBN number of the book"""
        for obj in book.book_list:
            if obj.isbn == isbn:
                print('Book with same ISBN exists, cannot add this book')
                return False
        return True

    if check_if_isbn_present(isbn):
        book_obj = book.BookClass(title=title, author=author, isbn=isbn, num_of_copies=no_of_copies)
        book.book_list.append(book_obj)
        dump_book_data()
        print(f'Book {title} added !')


def issue_book_student():
    """
    This function issue book to the student:
        1) Enter Student Roll No To Whom Book Has To Be Issued from user
        2) check if student present in library records
        3) find student with given data and check if he has reached book limit
        4) if limit reached goto step 12
        5) ask for book isbn
        6) check if given isbn is present and num copies of it are > 0 and also
              check is student has this book issued already or not(use check_available(book_isbn, std_roll):if
              not available go to step 11
        7) create a dict that will store isbn of book, and date of issue
        8) push created object into students issued books array(use modify_student(std_roll, issue_obj) )
        9) reached here means book has been issued successfully
        10) modify book details in library reduce copies(use modify_book(book_isbn))
        11) either isbn not present or all copies exhausted
        12) print('Student Has Reached Book Limit. Cannot Issue Book.')
        13) print('Student not found. Cannot Issue Book.')

    """
    roll = input('Enter Student Roll No To Whom Book Has To Be Issued : ')
    load_book_data()

    def check_roll_no(roll):
        """This function checks if roll no exists in library record or not
            and return student object, True or False and index of the student object in the student_list
        """
        i = -1
        for obj in student.student_data_list:
            i += 1
            if str(obj.roll_no) == roll:
                print('Student found !')
                return obj, True, i
        else:
            i = None
            print('Student not found !')
        return _, False, i

    stud, bool_roll_no, i = check_roll_no(roll)

    def check_book_limit(student_obj):
        """This fuction checks limit of the books issued to the student and return True and False"""

        if len(student_obj.book_issued) < 5:
            return True
        return False

    if bool_roll_no:
        if check_book_limit(stud):
            isbn = input('Enter book ISBN number : ')
            if len(isbn) != 13:
                print('Invalid ISBN !')
                return
            else:
                isbn = int(isbn)

            def check_if_isbn_present(isbn):
                """This function checks if ISBN exists in library record or not
                    and return True or False, book object and index of the student object in the student_list
                """

                i = -1
                for obj in book.book_list:
                    i += 1
                    if obj.isbn == isbn:
                        print('Book Found !')
                        return True, obj, i
                return False, _, None

            def check_number_of_copies(book_obj):
                """check if number of copy is greater than 0 or not, return True and False"""

                if book_obj.num_of_copies > 0:
                    return True
                else:
                    return False

            def check_book_already_issued(stud, book_obj):
                """checks if book already issued to the student or not"""
                for _ in stud.book_issued:
                    if _.isbn == book_obj.isbn:
                        print("You already have same copy ! , Can't issue another copy")
                        return False
                return True

            bool_isbn, book_obj, book_index = check_if_isbn_present(isbn)
            if bool_isbn:
                if check_number_of_copies(book_obj):
                    if check_book_already_issued(stud, book_obj):
                        book_dict = {book_obj.isbn : now.date()}
                        load_student_data()
                        student.student_data_list[i].book_issued.append(book_obj)
                        student.student_data_list[i].book_issued_details.append(book_dict)
                        book.book_list[book_index].num_of_copies -= 1
                        dump_book_data()
                        dump_student_data()
                        print('Book Issued !')
                else:
                    print('Book Not available !, Please try after sometime')
            else:
                print('Book ISBN not valid !, Please try again')
        else:
            print('You have reached book limit i.e 5, book cannot be issued to you')


def issue_book_faculty():
    """
    This function issue book to the faculty:
        1) Enter employee number to whom book has to be issues
        2) check if employee present in library record if not go to step12
        3) A faculty personal has no limit hence no need to check for anything We can simply issue book to him/her
        4) Enter Book ISBN That Has To Be Issued
        5) since faculty can issue more than one copy of book, we need to ask for num_copies as well
        6) Check if this book is present and its copies are >= num_copies by using
              function check_avail_faculty(book_isbn, num_copies):if not go to step 11
        7) Means book available with num copies Now just issue book to faculty create
              a dict that will store isbn of book, and date of issue and number of copies
        8) add book to faculty data by using by using modify_faculty(emp_id, issue_obj)
        9) modify book details in library by using modify_book(book_isbn, num_copies)
        10) printf('Book with {book_isbn} has been issued to employee with eid {emp_id}')
        11) print(f'Book with {book_isbn} not available/Copies Exhausted. Cannot issue book')
        12) print(f'Employee with {emp_id} not present. Cannot issue book.')
    """

    emp_id = input('Enter Employee Id To Whom Book Has To Be Issued : ')
    load_faculty_data()

    def check_emp_id(id):
        """This function checks if faculty with given id exists in library record or not."""

        i = -1
        for obj in faculty.faculty_list:
            i += 1
            if obj.e_id == int(id):
                print('Faculty found !')
                return obj, True, i
        else:
            i = None
            print('Faculty not found !')
        return _, False, i

    emp, bool_emp_id, i = check_emp_id(emp_id)

    if bool_emp_id:
        isbn = int(input('Enter book ISBN number : '))
        n_o_c = int(input('Enter number of copies : '))

        def check_if_isbn_present(isbn, n):
            """This function checks if book with given ISBN exists in library record or not and
            number of copies greater then 0 or not."""

            i = -1
            for obj in book.book_list:
                i += 1
                if obj.isbn == isbn and obj.num_of_copies >= n:
                    print('Book Found !')
                    return True, obj, i
            return False, _, None

        bool_isbn, book_obj, book_index = check_if_isbn_present(isbn, n_o_c)
        if bool_isbn:
            load_book_data()
            book_dict = {book_obj.isbn: [str(now.date()), n_o_c]}
            faculty.faculty_list[i].book_issued.append(book_dict)
            book.book_list[book_index].num_of_copies -= n_o_c
            dump_book_data()
            dump_faculty_data()
            print(f'Book with {isbn} has been issued to employee with eid {emp_id}')
        else:
            print(f'Book with {isbn} not available/Copies Exhausted. Cannot issue book')
    else:
        print(f'Employee with {emp_id} not present. Cannot issue book.')


def return_student():
    """This function return book from student and update student and book record."""
    # TODO
    # def check_fine():

    roll = input('Enter Student Roll No To return the book : ')
    load_student_data()

    def check_if_isbn_present(isbn_local):
        """This function check if book is present in book list or not."""
        i = -1
        for obj in book.book_list:
            i += 1
            if obj.isbn == isbn_local:
                print('Book Found !')
                return True, obj, i
        return False, _, None

    def check_roll_no(roll):
        """This function check if student with given roll number exists in library record or not"""

        i = -1
        for obj in student.student_data_list:
            i += 1
            if str(obj.roll_no) == roll:
                print('Student found !')
                return obj, True, i
        else:
            i = None
            print('Student not found !')
        return _, False, i

    stud, bool_roll_no, i = check_roll_no(roll)

    def check_book_student(isbn, i):
        """This function check if given book available in student book list or not"""
        j = -1
        for b in student.student_data_list[i].book_issued:
            j += 1
            if b.isbn == isbn:
                return True, j
        return False, None

    if bool_roll_no:
        isbn = int(input('Enter book ISBN number : '))
        bool_isbn, book_index = check_book_student(isbn, i)
        load_book_data()
        if bool_isbn:
            b_o = student.student_data_list[i].book_issued.pop(book_index)
            student.student_data_list[i].book_issued_details.pop(book_index)
            dump_student_data()

            bool_isbn2, book_obj, book_index2 = check_if_isbn_present(isbn)
            if bool_isbn2:
                book.book_list[book_index2].num_of_copies += 1
            else:
                b_o.num_of_copies += 1
                book.book_list.append(b_o)
            dump_book_data()
            print(f"Book {b_o.title} has been returned from {stud.name}")
        else:
            print(f"Student {stud.name} doesn't have book {isbn} ")


def return_faculty():
    """This function returns book by faculty."""

    emp_id = input('Enter Employee ID To return the book : ')
    load_faculty_data()

    def check_emp_id(id):
        """Verify given employee id from the faculty record."""
        i = -1
        for obj in faculty.faculty_list:
            i += 1
            if obj.e_id == int(id):
                print('Faculty found !')
                return obj, True, i
        else:
            i = None
            print('Faculty not found !')
        return _, False, i

    emp, bool_emp_id, i = check_emp_id(emp_id)

    def check_if_isbn_present(isbn_local):
        """check if book with given ISBN present or not"""
        i = -1
        for obj in book.book_list:
            i += 1
            if obj.isbn == isbn_local:
                print('Book Found !')
                return True, obj, i
        return False, _, None

    if bool_emp_id:
        isbn = int(input('Enter book ISBN number : '))

        def check_book_faculty(isbn_local, i):
            """Verify if faculty have given book or not."""
            j = -1
            for b in faculty.faculty_list[i].book_issued:
                l = list(b.keys())
                j += 1
                if l[0] == isbn_local:
                    return True, j
            return False, None
        bool_isbn, book_index = check_book_faculty(isbn, i)
        load_book_data()
        if bool_isbn:
            b_o = faculty.faculty_list[i].book_issued.pop(book_index)
            dump_faculty_data()
            here_isbn = int(list(b_o)[0])
            bool_isbn2, book_obj, book_index2 = check_if_isbn_present(here_isbn)
            book.book_list[book_index2].num_of_copies += b_o[here_isbn][1]
            dump_book_data()
            print(f'Faculty {emp.name} has returned books successfully')
        else:
            print(f"Faculty {emp_id} doesn't have book {isbn} ")


#     1) Retrieve book data from book pickle record
#     2) Use three modes to search data by isbn, author and title.
#     3) If book found print details of book


def book_search():
    """This function search the book by given criteria"""
    load_book_data()
    criteria, book_to_search = input('Enter Book to search (use format : isbn/author/title detail) : ').split(' ')
    if criteria == 'isbn':
        for _ in book.book_list:
            if _.isbn == int(book_to_search):
                print('BOOK FOUND !')
                print(_)
                break
        else:
            print('Book Not Available !')
    elif criteria == 'author':
        for _ in book.book_list:
            if _.author == book_to_search:
                print('BOOK FOUND !')
                print(_)
                break
        else:
            print('Book Not Available !')
    elif criteria == 'title':
        for _ in book.book_list:
            if _.title == book_to_search:
                print('BOOK FOUND !')
                print(_)
                break
        else:
            print('Book Not Available !')
    else:
        print('Wrong input ! please try again')


def print_student_records():
    """Print student record"""
    load_student_data()
    for _ in student.student_data_list:
        print(_)


def print_faculty_records():
    """Print faculty record"""
    load_faculty_data()
    for _ in faculty.faculty_list:
        print(_)


def print_book_records():
    """Print book record"""
    load_book_data()
    for _ in book.book_list:
        print(_)

