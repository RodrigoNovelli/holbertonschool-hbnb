from app.models.base import BaseModel
import re


class User(BaseModel):
    def __init__(self, first_name, last_name, email, password, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.password = password

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, string):
        if len(string) <= 50 and isinstance(string, str):
            self._first_name = string
        else:
            raise ValueError("""
                             First name must be a string and be under 50 char
                             """)

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, string):
        if len(string) <= 50 and isinstance(string, str):
            self._last_name = string
        else:
            raise ValueError('Last name must be a string and be under 50 char')

    @property
    def email(self):
        return self._email

    def validate_email(self, email):
        validator = r'^[a-zA-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(validator, email):
            return True
        else:
            return False

    @email.setter
    def email(self, string):
        if self.validate_email(string) is True:
            self._email = string
        else:
            raise ValueError('Invalid email')

    def add_places(self, places):
        self.places.append(places)
        places._owner = self
    
    def hash_password(self, password):
        """Hashes the password before storing it."""
        from app import bcrypt
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        from app import bcrypt
        return bcrypt.check_password_hash(self.password, password)
