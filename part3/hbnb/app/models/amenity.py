from app.models.base import BaseModel
from app import db
from sqlalchemy.orm import validates

class Amenity(BaseModel, db.Model):
    __tablename__ = 'amenity'
    name = db.Column(db.String(50), nullable=False)
    def __init__(self, name):
        super().__init__()
        self.name = name

    @validates("name")
    def validates_name(self, key, string):
        if len(string) <= 50:
            self.name = string
        else:
            raise ValueError('Name is too long')
