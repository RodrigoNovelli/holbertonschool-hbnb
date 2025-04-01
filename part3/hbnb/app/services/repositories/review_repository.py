from app.models.review import Review
from app import db
from app.persistence.repository import SQLAlchemyRepository

class ReviewRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Review)
    
    def get_review(self, review_id):
        return self.model.query.filter_by(review=review_id).first()