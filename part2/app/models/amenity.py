from . import BaseModel


class Amenity(BaseModel):
    def __init__(self.name):
        super().__init__()
        self.name = name

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, string):
        if len(string) <= 50:
            return self.name == string
        else:
            raise ValueError ('Amenity name cannot exceed 50 characters.')