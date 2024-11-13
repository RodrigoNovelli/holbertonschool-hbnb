from app.persistence.repository import InMemoryRepository

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
    list_a = self.amenity_repo.get_all()
    return list_a
    
    def update_amenity(self, amenity_id, amenity_data):
    update_a = self.amenity_repo.update(amenity_id, amenity_data)
    return update_a