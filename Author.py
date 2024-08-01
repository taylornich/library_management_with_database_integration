class author:
    def __init__(self, author_name, biography):
        self.__author_name = author_name
        self.__biography = biography
    
    def get_author_name(self):
        return self.__author_name
    
    def set_author_name(self, author_name):
        if not isinstance(author_name, str):
            raise ValueError("Author name must be a valid string")
        self.__author_name = author_name

    def get_biography(self):
        return self.__biography
    
    def set_biography(self, biography):
        if not isinstance(biography, str):
            raise ValueError("Biography must be a valid string")
        self.__biography = biography