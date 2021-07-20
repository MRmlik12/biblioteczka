"""User domain"""
from datetime import datetime
from uuid import UUID, uuid4

from pydantic.networks import EmailStr

from catana.services import hash


class Address:
    """Address entity"""

    street_number: str
    local: str
    postal_code: int
    city: str


class User:
    """User entity"""

    id: UUID
    email: EmailStr
    date_created: datetime
    username: str
    surname: str
    phone_number: str


class UserInDb(User):
    """User db operations"""

    salt: str
    hashed_password: str

    def generate_id(self) -> None:
        """Generate user id"""
        self.id = uuid4()

    def create_timestamp(self):
        """Create timestamp"""
        self.date_created = datetime.utcnow()

    def create_password_hash(self, password: str):
        """create password hash"""
        self.salt = hash.generate_salt()
        self.hashed_password = hash.get_hash(self.salt + password)

    def check_password_hash(self, password: str) -> bool:
        """Checks password hash"""
        return hash.verify_hash(self.salt + password, self.hashed_password)
