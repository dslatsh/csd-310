"""
    Title: whatabook.py
    Author: Devin Latshaw
    Date: 7/16/2022
    Description: The whatabook program which is a console that allows interface
                 with a MySQL database and allows user response
"""

# Import statements
import sys
from time import sleep
import mysql.connector
from mysql.connector import errorcode

# Configuration for the database connection
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

""" Next we will be doing def (definition) statements for the various tasks """

# Defining the display menu for the program
def show_menu():
    print("\n -- Main Menu --")

    print("\n   1. View Books\n   2. View Store Locations\n   3. My Account\n   4. Exit Program")

    try:
        choice = int(input('\n  Please input your choice  <Example, Enter: 2 for store locations>: '))

        return choice
    except ValueError:
        print("\n     Invalid number, program is exiting!\n")
        sleep(5)
        sys.exit(0)

# Defining the displaying of the books program using an inner join query
def show_books(_cursor):
    _cursor.execute("SELECT book_id, book_name, author, details FROM book")

    # Getting results form cursor object
    books = _cursor.fetchall()

    # Printing the header
    print("\n   -- BOOK LISTING --")

    # Using a for loop to iterate over the books to display
    for book in books:
        print("\n     Book ID: {}\n     Book Name: {}\n     Author: {}\n     Details: {}\n".format(book[0], book[1], book[2], book[3]))

# Defining the display locations program
def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale FROM store")

    locations = _cursor.fetchall()

    print("\n   -- STORE LOCATIONS --")

    for location in locations:
        print("\n   Locale: {}\n".format(location[1]))

# Defining the user validation program
def validate_user():
    while True:
        try:
            user_id = int(input('\n     Please enter your customer ID <Example - Enter 1 for user_id 1>: '))

            if user_id <= 0 or user_id >= 4:
                print("\n     Invalid customer number ID, please try again!\n")
                continue
            else:
                return user_id              
            
        
            
        except ValueError:
            print("\n     Invalid number, program is exiting!\n")
            sleep(5)
            sys.exit(0)
    
        
# Defining account menu program to display user's account menu
def show_account_menu():
    try:
        print("\n     --  Customer Menu --")
        print("\n     1. Wish List\n     2. Add Book\n     3. Delete Book\n     4. Main Menu")
        cust_selectionion = int(input('\n   Please input your choice  <Example, Enter: 2 for store locations>: '))

        return cust_selectionion
    
    except ValueError:
        print("\n     Invalid number, program is exiting!\n")
        sleep(5)
        sys.exit(0)

# Defining the show wish list selection for books added to the user's wishlist
def show_wishlist(_cursor, user_id):
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(user_id))
    wishlist = _cursor.fetchall()

    print("\n       -- WISH LIST ITEMS --\n")
    
    for book in wishlist:
        print("     Book ID: {}\n     Book Name: {}\n     Author: {}\n".format(book[3], book[4], book[5]))

# Defining the showing of books that are not in the users wish list via query (qry)
def show_books_to_add(_cursor, user_id):
    qry = ("SELECT book_id, book_name, author, details "
           "FROM book "
           "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(user_id))

    print(qry)

    _cursor.execute(qry)

    books_available = _cursor.fetchall()

    print("\n     -- Available Books To Add --\n")

    for book in books_available:
        print("     Book ID: {}\n       Book Name: {}\n".format(book[0], book[1]))

# Defining the adding of a book to wishlist
def add_book_to_wishlist(_cursor, user_id, book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(user_id, book_id))

def show_books_to_delete(_cursor, user_id):
    qry = ("SELECT book_id, book_name, author, details "
           "FROM book "
           "WHERE book_id IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(user_id))
    
    print(qry)

    _cursor.execute(qry)

    books_available = _cursor.fetchall()

    print("\n   -- Available Books to Delete --\n")

    for book in books_available:
        print("     Book ID: {}\n       Book Name: {}\n".format(book[0], book[1]))
    
def del_book_from_wishlist(_cursor, user_id, book_id):
    _cursor.execute("DELETE FROM wishlist WHERE user_id = {} AND book_id = {}".format(user_id, book_id))
           
try:
    
    # Connect to the WhatABook database 

    db = mysql.connector.connect(**config) 
    
    cursor = db.cursor()

    print("\n  Welcome to the WhatABook Application! ")

    # Show the main menu and take user's response
    users_choice = show_menu() 

    # while statement for if user's choice is not 4
    while users_choice != 4:

        # Choice 1 goes to show_books program
        if users_choice == 1:
            show_books(cursor)

        # Choice 2 goes to show_locations program
        if users_choice == 2:
            show_locations(cursor)

        # Choice 3 is the user's menu program
        if users_choice == 3:
            my_user_id = validate_user()
            cust_selection = show_account_menu()

            # while account option does not equal 3
            while cust_selection != 4:

                # Choice 1 is to show the user's wishlist
                if cust_selection == 1:
                    show_wishlist(cursor, my_user_id)

                # Choice 2 calls the show_books_to_add function
                if cust_selection == 2:

                    # Show the books not currently in the users wish list
                    show_books_to_add(cursor, my_user_id)

                    # Retrieve entered book ID 
                    try:
                        book_id = int(input("\n        Enter the id of the book you want to add: "))
                    except ValueError:
                        print("\n     Invalid number, program is exiting!\n")
                        sleep(5)
                        sys.exit(0)
                    
                    # This will add the selected book to the wish list
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    # Commits the change to the DB
                    db.commit() 

                    print("\n        Book id: {} was added to your wish list!".format(book_id))
                                # Choice 2 calls the show_books_to_add function
                
                # Choice 3 calls the show_books_to_delete
                if cust_selection == 3:

                    # Show the books not currently in the users wish list
                    show_books_to_delete(cursor, my_user_id)

                    # Retrieve entered book ID 
                    try:
                        book_id = int(input("\n        Enter the id of the book you want to delete: "))
                    except ValueError:
                        print("\n     Invalid number, program is exiting!\n")
                        sleep(5)
                        sys.exit(0)
                    
                    # This will add the selected book to the wish list
                    del_book_from_wishlist(cursor, my_user_id, book_id)

                    # Commits the change to the DB
                    db.commit() 

                    print("\n        Book id: {} was deleted to your wish list!".format(book_id))

                # If user's choice is less than 0 or greater than 4, display an invalid user selection
                if cust_selection < 0 or cust_selection > 4:
                    print("\n      Invalid selection made, please retry!")

                # Show the account menu 
                cust_selection = show_account_menu()
               
        
        # If user's choice is less than 0 or greater than 4, display an invalid user selection
        if users_choice < 0 or users_choice > 4:
            print("\n      Invalid selection made, please retry!")
        
        # Show the main menu
        users_choice = show_menu()
    
    print("\n\n  Program terminated...")
    sleep(5)
except mysql.connector.Error as err:
    """ handle errors """ 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()

