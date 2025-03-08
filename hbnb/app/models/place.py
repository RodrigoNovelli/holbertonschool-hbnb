from app.models.base import BaseModel
from app.models.amenity import Amenity
from app.models.user import User


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner, owner_id, amenities):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.owner = owner
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, string):
        if len(string) <= 100 and isinstance(string, str):
            self._title = string
        else:
            raise ValueError('Title must be a string under 100 char')
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, string):
        if isinstance(string, str):
            self._description = string
        else:
            raise ValueError('Description must be a string')

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, num):
        if num > 0 and isinstance(num, float):
            self._price = num
        else:
            raise ValueError('Price must be a positive float')
    
    @property
    def latitude(self):
        return self._latitude
    
    @latitude.setter
    def latitude(self, num):
        if num <= 90.0 and num >= -90.0 and isinstance(num, float):
            self._latitude = num
        else:
            raise ValueError('Latitude must be between -90.0 and 90.0')
    
    @property
    def longitude(self):
        return self._longitude
    
    @longitude.setter
    def longitude(self, num):
        if num >= -180.0 and num <= 180.0 and isinstance(num, float):
            self._longitude = num
        else:
            raise ValueError('Longitude must be between -180.0 and 180.0')
    
    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
    
    def get_amenity(self):
        return self.amenities
