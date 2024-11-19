#!/usr/bin/python3
from . import BaseModel
from app.models.user import User
from app.models.amenity import amenity


class Place(BaseModel):
    places = []

    def __init__(self, title: str, description: str, price: float, latitude: float, longitude: float, owner: User, amenities=None):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []  # List to store related reviews
        if amenities is None:
            self.amenities = []  # List to store related amenities
        else:
            self.amenities = amenities
        self.validate()

    @property
    def title(self):
        return self.title

    @title.setter
    def title (self, value):
        if len(value) >= 100:
            raise ValueError("Title is too long")
        else:
            self.title = value
    
    @property
    def price(self):
        return self.price
    
    @price.setter
    def price (self, value):
        if not isinstance (value, float):
            raise ValueError("invalid type value")
        else:
            self.price = abs(value)
    
    @property
    def latitude(self):
        return self.latitude
    
    @latitude.setter
    def latitude(self, value):
        if value >= -90 and value <= 90:
            self.latitude = value
        else:
            raise ValueError("latitude is out of range")
    
    @property
    def longitude(self):
        return self.longitude
    
    @longitude.setter
    def longitude(self, value):
        if value >= -180 and value <= 180:
            self.longitude = value
        else:
            raise ValueError("longitude is out of range")

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
    
    def get_amenities(self):
        return self.amenities
    
    @classmethod
    def add_place(cls, place):
        cls.places.append(place)