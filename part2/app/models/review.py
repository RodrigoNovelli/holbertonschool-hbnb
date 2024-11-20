from . import BaseModel
from app.models.place import Place
from app.models.user import User


class Review (BaseModel):
    def __init__(self, text: str, rating: int, place: Place, user: User):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
        self.validate()
    
    @property
    def rating(self):
        return self.rating
    
    @rating.setter
    def rating(self, value):
        if self.value >= 1 and self.value <= 5:
            self.rating = value
        else:
            raise ValueError ("Raiting must between 1 and 5")