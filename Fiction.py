from Book import book

class fiction(book):
    def __init__(self, title, author, isbn, pub_date, genre, category):
        super().__init__(title, author, isbn, pub_date, genre)
        self.__category = category

    def get_category(self):
        return self.__category
    
    def set_category(self, category):
        self.__category = category