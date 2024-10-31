from . import BaseModel
from app.models.user import User
from app.models.amenity import amenity


class Place(BaseModel):
    def __init__(self, title: str, description: str, price: float, latitude: float, longitude: float, owner: User, amenities=None):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities
        self.validate()

        def validate(self):
        if len(self.title) > 100:
            raise ValueError("Title cannot exceed 100 characters.")
        if self.price <= 0:
            raise ValueError("Price must be a poitive value.")
        if not (-90.0 <= self.latitude <= 90.0):
            raise ValueError("Latitude must be between -90 and 90.")
        if not (-180.0 <= self.longitude <= 180.0):
            raise ValueError("Longitude must be between -180 and 180.")

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)