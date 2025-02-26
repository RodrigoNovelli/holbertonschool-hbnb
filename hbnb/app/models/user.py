from . import BaseModel
import re

class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin= False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
    
    @property
    def first_name(self):
        return self.first_name
    
    @first_name.setter
    def first_name(self, string):
        if len(string) <= 50 and isinstance(string, str):
            self.first_name = string
        else:
            raise ValueError('First name must be a string and be under 50 char')    
    @property
    def last_name(self):
        return self.last_name
    
    @last_name.setter
    def last_name(self, string):
        if len(string) <= 50 and isintance(string, str):
            self.last_name = string
        else:
            raise ValueError('Last name must be a string and be under 50 char')
    
    @property
    def email(self):
        return self.email
    
    @email.setter
    def email(self, string):
        if validate_email(string) == True:
            self.email = string
        else:
            raise ValueError('Invalid email')
        
    
    def validate_email(self, email):
                validator = r'^[a-zA-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
                if re.match(validator, email):
                    return email
                else:
                    raise ValueError("Invalid email")
    
    def add_places(self, places):
        self.places.append(places)
        places.owner = self
    
    
    
    

        