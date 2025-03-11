from app.persistence.repository import InMemoryRepository
from app.api.v1 import users
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review
class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
    
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
        return self.user_repo.get_by_attribute('email', email)
    
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

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
    
    def create_review(self, review_data):
        # We get user and place id related to the review
        user_id = review_data.pop('user_id')
        place_id = review_data.pop('place_id')

        # Verify if User and Place exists
        user_list = get_user(user_id)
        r_user = None
        for user in user_list:
            if user.id == user_id:
                r_user = user
                break
        places_list = Place.get_places()
        r_place = None
        for place in places_list:
            if place.id == place_id:
                r_place = place
                break
        # If doesn't exist raises ValueError
        if r_user is None or r_place is None:
            raise ValueError(f"User with id {user_id} or Place with id {place_id} not found")

        # Preparing review package for instance initialization
        review_data['user'] = r_user
        review_data['place'] = r_place
        new_review = Review(**review_data)
        r_place.add_review(new_review)
        self.review_repo.add(new_review)
        return new_review


    def get_place(self, place_id):
        return self.place_repo.get(place_id)


    def get_all_places(self):
        list_p = self.place_repo.get_all()
        return list_p

    def update_place(self, place_id, place_data):
        update_p = self.place_repo.update(place_id, place_data)
        return update_p
    
    # Gets a Review by ID
    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    # Gets all Reviews
    def get_all_reviews(self):
        reviews = self.review_repo.get_all()
        return [
            {
                "id": review.id,
                "text": review.text,
                "rating": review.rating
            }
             for review in reviews]

    # Gets Reviews by Place Attribute
    def get_reviews_by_place(self, place_id):
        review_list = Review.get_review_list()
        return [
            {
                "id": review.id,
                "text": review.text,
                "rating": review.rating
            }
             for review in review_list if review.place.id == place_id]

    # Updates a Review
    def update_review(self, review_id, review_data):
        return self.review_repo.update(review_id, review_data)
