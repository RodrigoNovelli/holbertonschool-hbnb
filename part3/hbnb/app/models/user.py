from app import db
from app.models.base import BaseModel
import re
from sqlalchemy.orm import validates
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class User(BaseModel, db.Model):
    __tablename__ = 'users'

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, first_name, last_name, email, password, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.password = self.hash_password(password)

    @validates("first_name")
    def validates_first_name(self, key, string):
        if len(string) <= 50 and isinstance(string, str):
            return string
        else:
            raise ValueError("""
                             First name must be a string and be under 50 char
                             """)

    @validates("last_name")
    def validates_last_name(self, key, string):
        if len(string) <= 50 and isinstance(string, str):
            return string
        else:
            raise ValueError('Last name must be a string and be under 50 char')

    def validate_email(self, email):
        validator = r'^[a-zA-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(validator, email):
            return True
        else:
            return False

    @validates("email")
    def validates_email(self, key, string):
        if self.validate_email(string) is True:
            return string
        else:
            raise ValueError('Invalid email')

    def add_places(self, places):
        self.places.append(places)
        places.owner = self

    @validates("password")
    def hash_password(self, key, password):
        """Hashes the password before storing it."""
        return bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)
