from . import BaseModel
import re

class User(BaseModel):
    def __init__(self, first_name: str, last_name: str, email: str, is_admin=False):
        super().__init__() # Llama al constructor de la super clase
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.validate() # Valida los atrivutos

    def validate(self):
        if len(self.first_name) > 50:
            raise ValueError("First name cannot exceed 50 characters.")
        if len(self.last_name) > 50:
            raise ValueError("Last name cannot exceed 50 characters.")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            raise ValueError("Invalid email format.")
