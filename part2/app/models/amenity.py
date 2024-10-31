from . import BaseModel


class Amenity(BaseModel):
    def __init__(self.name):
        super().__init__()
        self.name = name
        self.validate()

    def validate(self):
        if len(self.name) > 50:
            raise ValueError("Amenity name cannot exceed 50 characters.")
