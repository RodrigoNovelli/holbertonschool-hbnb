from app.models.base import BaseModel
from app.models.user import User
from app.models.place import Place


class Review(BaseModel):
    def __init__(self, text, rating, place_id, user_id):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id
    
    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, string):
        if isinstance(string, str):
            self._text = string
            print("logrado")
        else:
            raise ValueError("Text must be a string")
    
    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, num):
        if num <= 5 and num >= 1 and isinstance(num, int):
            self._rating = num
            print("logrado2")
        else:
            raise ValueError('Rating mus be a number between 1 and 5')
    
    
