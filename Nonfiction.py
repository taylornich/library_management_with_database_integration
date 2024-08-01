from Book import book

class nonfiction:
    def __init__(self, title, author, isbn, pub_date, genre, expertise):
        super().__init__(title, author, isbn, pub_date, genre)
        self.__expertise = expertise

    def get_expertise(self):
        return self.__expertise
    
    def set_expertise(self, expertise):
        self.__expertise = expertise