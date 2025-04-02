from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review
from app.persistence.repository import SQLAlchemyRepository
from app.services.repositories.user_repository import UserRepository
from app.services.repositories.place_repository import PlaceRepository
from app.services.repositories.review_repository import ReviewRepository
from app.services.repositories.amenity_repository import AmenityRepository
class HBnBFacade:
    def __init__(self):
        self.user_repo = UserRepository
        self.place_repo = PlaceRepository
        self.review_repo = ReviewRepository
        self.amenity_repo = AmenityRepository
    
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_users_list(self):
        users = self.user_repo.get_all()
        return [user.to_dict() for user in users]

    def get_user_by_email(self, email):
        return self.user_repo.get_user_by_email(email)

    def update_user(self, user_id, user_data):
        update = self.user_repo.update(user_id, user_data)
        return update

    def create_amenity(self, amenity_data):
        amenity_name = amenity_data.get('name')
        new_amenity = Amenity(amenity_name)
        self.amenity_repo.add(new_amenity)
        return new_amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        updated_a = self.amenity_repo.update(amenity_id, amenity_data)
        return updated_a


    def create_place(self, place_data):
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get_place(place_id)


    def get_all_places(self):
        list_p = self.place_repo.get_all()
        return list_p

    def update_place(self, place_id, place_data):
        update_p = self.place_repo.update(place_id, place_data)
        return update_p

    def delete_place(self, place_id):
        self.place_repo.delete(place_id)

    def create_review(self, review_data):
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)
    
    def get_all_reviews(self):
        reviewlist = self.review_repo.get_all()
        return reviewlist

    def get_reviews_by_place(self, place_id):
        reviews = self.get_all_reviews()
        list = []
        for review in reviews:
            if review.place_id == place_id:
                list.append(review)
            return list

    def update_review(self, review_id, review_data):
        updatedreview = self.review_repo.update(review_id, review_data)
        return updatedreview

    def delete_review(self, review_id):
        self.review_repo.delete(review_id)
