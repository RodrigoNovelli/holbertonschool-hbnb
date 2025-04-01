from app.models.amenity import Amenity
from app import db
from app.persistence.repository import SQLAlchemyRepository

class AmenityRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Amenity)
    
    def get_amenity(self, amenity_id):
        return self.model.query.filter_by(Amenity=amenity_id).first()