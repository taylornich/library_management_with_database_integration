class genre:

    def __init__(self, genre_name, description, category):
        self.__genre_name = genre_name
        self.__description = description
        self.__category = category

    def get_genre_name(self):
        return self.__genre_name
    
    def set_genre_name(self, genre_name):
        if not isinstance(genre_name, str):
            raise ValueError("Genre must be a valid string")
        self.__genre_name = genre_name
    
    def get_description(self):
        return self.__description
    
    def set_description(self, description):
        if not isinstance(description, str):
            raise ValueError("Description must be a valid string")
        self.__description = description
    
    def get_category(self):
        return self.__category
    
    def set_category(self, category):
        if not isinstance(category, str):
            raise ValueError("Category must be a valid string")
        self.__category = category
    