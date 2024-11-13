from . import BaseModel
import re

class User(BaseModel):
    def __init__(self, first_name: str, last_name: str, email: str, is_admin=False):
        super().__init__() # Llama al constructor de la super clase
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.places = []
        User.user_list.append(self)

        @property
        def first_name(self):
        return self.first_name

        @first_name.setter
        def first_name(self, string):
            if len(sting) <= 50 and isinstance(string, str):
                self.first_name = string
            else:
                raise ValueError('Name cannot exceed 50 characters')
        
        @property
        def last_name(self):
            return self.last_name
        
        @last_name.setter
        def last_name(self, string):
            if len(string) <= 50 and isinstance(string, str):
                self.last_name = string
            else:
                raise ValueError('Last name cannot exceed 50 characters')
        
        @property
        def email(self):
            return selg.email
        
        @email.setter
        def email(self, value):
            if self.validate_email(value) == True:
                self.email = value
            else:
                raise ValueError('Invalid email')
        
        def validate_email(self, email):
            validator = r'^[a-zA-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if re.match(validator, email):
                return email
            else:
                raise ValueError("Invalid email") 
        
        def add_places(self, places):
            self.places.append(place)
            place.owner = self
        
        def get_user_list(self):
            return User.user_list