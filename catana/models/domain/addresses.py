"""Address"""
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import TIMESTAMP, String

from catana.models.domain.base import Base


class Address(Base):
    """Address entity"""

    __tablename__ = "addresses"
    user_id = Column("user_id", (UUID(as_uuid=True)), primary_key=True)
    street = Column("street", String, nullable=False)
    local_no = Column("local_no", String, nullable=False)
    town = Column("town", String, nullable=False)
    postal_code = Column("postal_code", String, nullable=False)
    updated_at = Column("updated_at", TIMESTAMP, nullable=True)


class AddressesInDb(Address):
    """Addresses db operation"""
