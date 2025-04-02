from app.models.base import BaseModel
from app.models.user import User
from app.models.place import Place
from app import db
from sqlalchemy.orm import validates, relationship
from sqlalchemy import Table, Column, Integer, ForeignKey


class Review(BaseModel):
    __tablename__ = 'review'

    text = db.Column(db.String(125), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    place_id = Column(Integer, ForeignKey('place.id'), nullable=False)
    user = relationship('User', back_populates='reviews')
    place = relationship('Place', back_populates='reviews')

    def __init__(self, text, rating, place_id, user_id):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id
    
    
    @validates("text")
    def validate_text(self, key, string):
        if isinstance(string, str):
            return string
        else:
            raise ValueError("Text must be a string")
    
    
    @validates("rating")
    def validate_rating(self, key, num):
        if num <= 5 and num >= 1 and isinstance(num, int):
            return num
        else:
            raise ValueError('Rating mus be a number between 1 and 5')
    
    
