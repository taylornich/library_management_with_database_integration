class user:

    def __init__(self, name, user_id):
        self.__name = name
        self.__user_id = user_id
        self.__books_borrowed = []

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError("Please enter your name as a valid string")
        self.__name = name

    def get_user_id(self):
        return self.__user_id
    
    def set_user_id(self, user_id):
        if not isinstance(user_id, str):
            raise ValueError("User ID must be a valid string")
        self.__user_id = user_id
    
    def get_books_borrowed(self):
        return self.__books_borrowed
    
    def books_borrowed(self, book):
        if book.is_available():
            self.__books_borrowed.append(book)
            book.set_available = False
        else:
            print("Sorry, book is not available")
    
    def return_book(self, book):
        if book in self.__books_borrowed:
            self.__books_borrowed.remove(book)
            book.set_availability = True
        else:
            print("The user did not borrow this book and therefore cannot return it.")
