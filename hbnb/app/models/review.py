from . import BaseModel
from . import User
from . import Place


class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
    
    @property
    def text(self):
        return self.text
    
    @text.settter
    def text(self, string):
        if isinstance(string, str):
            self.text = string
        else:
            raise ValueError("Text must be a string")
    
    @property
    def rating(self):
        return rating
    
    @rating.setter
    def rating(self, num):
        if num <= 5 and num >= 1 and isinstance(num, int):
            self.rating = num
        else:
            raise ValueError('Rating mus be a number between 1 and 5')
    
    
