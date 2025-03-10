from app.persistence.repository import InMemoryRepository
from app.api.v1 import users
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
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


    def get_place(self, place_id):
        return self.place_repo.get(place_id)


    def get_all_places(self):
        list_p = self.place_repo.get_all()
        return list_p

    def update_place(self, place_id, place_data):
        update_p = self.place_repo.update(place_id, place_data)
        return update_p
