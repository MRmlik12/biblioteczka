from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from sqlalchemy.sql.functions import user

from catana.models.common import IDModel
from catana.models.schemas.users import UserInRegister
from catana.services import hash


class Address:
    street_number: str
    local: str
    postal_code: int
    city: str


class User(IDModel):
    id: UUID
    email: str
    date_created: datetime
    username: str
    surname: str
    phone_number: str


class UserInDb(User):
    salt: str
    hashed_password: str

    def __init__(self, user_register: UserInRegister):
        self.email = user_register.email
        self.username = user_register.name
        self.surname = user_register.surname
        self.phone_number = user_register.phone_number

    def generate_id(self) -> None:
        self.id = uuid4()

    def create_timestamp(self):
        self.date_created = datetime.utcnow()

    def create_password_hash(self, password: str):
        self.salt = hash.generate_salt()
        self.hashed_password = hash.get_hash(self.salt + password)

    def check_password_hash(self, password: str) -> str:
        return hash.verify_hash(self.hash + password, self.hashed_password)
