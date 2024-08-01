class book:
    def __init__(self, title, author, ISBN, pub_date, genre):
        self.__title = title
        self.__author = author
        self.__ISBN = ISBN
        self.__pub_date = pub_date
        self.__genre = genre
        self.__available = True

    def get_title(self):
        return self.__title
    
    def set_title(self, title):
        if not isinstance(title, str):
            raise ValueError("Title name must be a valid string.")
        self.__title = title

    def get_author(self):
        return self.__author
    
    def set_author(self, author):
        if not isinstance(author, str):
            raise ValueError("Author's name must be a valid string.")
        self.__author = author
    
    def get_ISBN(self):
        return self.__ISBN
    
    def set_ISBN(self, ISBN):
        if not (isinstance(ISBN, int) and len(ISBN) == 13):
            raise ValueError("ISBN must be a valid thirteen digit integer")
        self.__ISBN = ISBN
    
    def get_pub_date(self):
        return self.__pub_date
    
    def set_pub_date(self, pub_date):
        if not isinstance(pub_date, int):
            raise ValueError("Publication date must be entered in valid integer format")
        self.__pub_date = pub_date
    
    def get_genre(self):
        return self.__genre
    
    def set_genre(self, genre):
        if not isinstance(genre, str):
            raise ValueError("Genre must be a vaid string")
        self.__genre = genre


    def is_available(self):
        return self.__available
    
    def set_availability(self, available):
        self.__available = available
