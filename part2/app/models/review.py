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
    
    def validate():
        if not (1 <= self.raitig <= 5):
            raise ValueError("Rating must be between 1 and 5")
