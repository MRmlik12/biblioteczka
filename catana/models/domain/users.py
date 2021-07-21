"""User domain"""
from catana.models.domain.base import Base
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import String

from catana.services import hash


class User(Base):
    """User entity"""

    __tablename__ = "users"

    id = Column("id", (UUID(as_uuid=True)), primary_key=True, default=uuid4)
    username = Column("username", String, nullable=False)
    surname = Column("surname", String, nullable=False)
    email = Column("email", String, nullable=False)
    salt = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    phone_number = Column("phone_number", String, nullable=False)
    created_at = Column("created_at", TIMESTAMP)
    updated_at = Column("updated_at", TIMESTAMP)


class UserInDb(User):
    """User db operations"""

    def generate_id(self) -> None:
        """Generate user id"""
        self.id = uuid4()

    def create_timestamp(self):
        """Create timestamp"""
        self.created_at = datetime.utcnow()

    def create_password_hash(self, password: str):
        """create password hash"""
        self.salt = hash.generate_salt()
        self.hashed_password = hash.get_hash(self.salt + password)

    def check_password_hash(self, password: str) -> bool:
        """Checks password hash"""
        return hash.verify_hash(self.salt + password, self.hashed_password)
