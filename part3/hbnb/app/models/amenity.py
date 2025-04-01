from app.models.base import BaseModel
from app import db

class Amenity(BaseModel, db.Model):
    __tablename__ = 'amenity'
    name = db.Column(db.String(50), nullable=False)
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, string):
        if len(string) <= 50 and isinstance(string, str):
            self._name = string
        else:
            raise ValueError('Name must be a string between 0 and 50 char')
