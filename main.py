from Functions import *
import pickle, sys
import getpass as gp
exit = True


def menu():
    while True:
        print('<<<<<<<<<<<< MAIN MENU >>>>>>>>>>>>')
        print('\t1. Add Student \n'
              '\t2. Add Faculty \n'
              '\t3. Add Book \n'
              '\t4. Issue book to the student \n'
              '\t5. Issue book to the faculty \n'
              '\t6. Return book by Student \n'
              '\t7. Return book by Faculty\n'
              '\t8. Search Book\n'
              '\t9. Print Student records\n'
              '\t10. Print Faculty record\n'
              '\t11. Print Book record\n'
              '\t12. Exit\n'
              '\t13. Change Admin\n')
        choice = int(input())
        if choice == 1:
            add_student()
            print('\n')
        elif choice == 2:
            add_faculty()
            print('\n')
        elif choice == 3:
            add_book()
            print('\n')
        elif choice == 4:
            issue_book_student()
            print('\n')
        elif choice == 5:
            issue_book_faculty()
            print('\n')
        elif choice == 6:
            return_student()
            print('\n')
        elif choice == 7:
            return_faculty()
            print('\n')
        elif choice == 8:
            book_search()
            print('\n')
        elif choice == 9:
            print_student_records()
            print('\n')
        elif choice == 10:
            print_faculty_records()
            print('\n')
        elif choice == 11:
            print_book_records()
            print('\n')
        elif choice == 12:
            print('Exiting................... ')
            sys.exit()
        elif choice == 13:
            change_id_pass()
            print('\n')
        print('\n')
        print('****************************************')


def change_id_pass():
    """Change Librarian ID and Password"""

    with open('login_data.pkl', 'rb') as f:
        str_obj = pickle.load(f)
    user_id, passwd = str_obj.split('@')
    admin_id = input('Enter Librarian User ID : ')
    if user_id == admin_id:
        password = gp.getpass('Enter Password : ', '*')
        if password == passwd:
            admin_id_new = input('Enter New Librarian user id : ')
            password = gp.getpass('Enter New Password : ', '*')
            str_obj = admin_id_new + '@' + password
            with open('login_data.pkl', 'wb') as f:
                pickle.dump(str_obj, f)
            print(f'Admin Changed from {admin_id} to {admin_id_new}')
    else:
        print('Invalid User Id !')


def log_in():
    """Login to the system"""
    with open('login_data.pkl', 'rb') as f:
        str_obj = pickle.load(f)
    user_id, passwd = str_obj.split('@')
    admin_id = input('Enter Librarian User ID : ')
    if user_id == admin_id:
        password = gp.getpass('Enter Password : ', '*')
        if password == passwd:
            menu()
    else:
        print('Invalid User Id !')


log_in()
