from app.models.base import BaseModel
from app.models.amenity import Amenity
from app.models.user import User
from app import db
from sqlalchemy.orm import validates, relationsip


class Place(BaseModel, db.Model):
    __tablename__ = 'places'
    tile = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    
    def __init__(self, title, description, price, latitude, longitude, owner, owner_id, amenities):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.owner = owner
        self.reviews = []
        if amenities is None:# List to store related reviews
            self.amenities = []  # List to store related amenities
        else:
            self.amenities = amenities

    @validates("title")
    def validates_nametitle(self, key, string):
        if len(string) <= 100:
            self.title = string
        else:
            raise ValueError('Title is too long')
    
    @validates("description")
    def validates_description(self, key, string):
        if isinstance(string, str):
            self.description = string
        else:
            raise ValueError('Description must be a string')

    @validates("price")
    def validates_price(self, key,  value):
        if not isinstance(value, float):
            self.price = value
        else:
            raise ValueError('Price must be a positive float')
    
    @validates("latitude")
    def validates_latitude(self, key, num):
        if num <= 90.0 and num >= -90.0 and isinstance(num, float):
            self.latitude = num
        else:
            raise ValueError('Latitude must be between -90.0 and 90.0')
        
    @validates("longitude")
    def validates_longitude(self, key, num):
        if num >= -180.0 and num <= 180.0 and isinstance(num, float):
            self.longitude = num
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
