import book_operations
import user_operations
import author_operations
import genre_operations


    
def mainMenu():
    while True:
        print('''Welcome to the Library Management System!
                
            Main Menu:
            1. Book Operations
            2. User Operations
            3. Author Operations
            4. Genre Operations
            5. Quit''')

        menu_choice = input("Enter your choice in 1-5 format:")
        

        if menu_choice == '1':
            book_menu()
        elif menu_choice == '2':
            user_menu()
        elif menu_choice == '3':
            author_menu()
        elif menu_choice == '4':
            genre_menu()
        elif menu_choice == '5':
            print("Quitting application")
            break
        else:
            print("Invalid menu option")


def book_menu():
    print('''Book Operations:
            1. Add a new book
            2. Borrow a book
            3. Return a book
            4. Search for a book
            5. Display all books''')
    
    book_menu_choice = input("Please enter your choice 1-5:")

    if book_menu_choice == '1':
        book_operations.add_book()
    elif book_menu_choice == '2':
        book_operations.borrow_book()
    elif book_menu_choice == '3':
        book_operations.return_book()
    elif book_menu_choice == '4':
        book_operations.search_book()
    elif book_menu_choice == '5':
        book_operations.display_books()
    else:
        print("Please only enter choice as an int, 1-5.")

def user_menu():
    print('''User Operations:
            1. Add a new user
            2. View user details
            3. Display all users''')
    
    user_menu_choice = input("Please enter your choice 1-3: ")

    if user_menu_choice == '1':
        user_operations.add_user()
    elif user_menu_choice == '2':
        user_operations.view_user_details()
    elif user_menu_choice == '3':
        user_operations.display_users()
    else:
        print("Please only enter choice as an int, 1-3.")

def author_menu():
    print('''User Operations:
            1. Add a new author
            2. View author details
            3. Display all authors''')
    
    author_menu_choice = input("Please enter your choice 1-3")

    if author_menu_choice == '1':
        author_operations.add_author()
    elif author_menu_choice == '2':
        author_operations.view_author_details()
    elif author_menu_choice == '3':
        author_operations.display_authors()
    else:
        print("Please only enter chioice as an int, 1-3.")


def genre_menu():
    print('''Genre Operations:
            1. Add a new genre
            2. View genre details
            3.Display all genres''')
    
    genre_menu_choice = input("Please enter your choice 1-3")

    if genre_menu_choice == '1':
        genre_operations.add_genre()
    elif genre_menu_choice == '2':
        genre_operations.view_genre_details()
    elif genre_menu_choice == '3':
        genre_operations.display_genres()
    else:
        print("Please only enter choice as an int, 1-3.")

if __name__ == "__main__":
    mainMenu()