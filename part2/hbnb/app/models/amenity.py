from app.models.base import BaseModel


class Amenity(BaseModel):
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
