"""Address"""
from uuid import UUID

from fastapi_sqlalchemy import db

from catana.models.domain.addresses import AddressesInDb
from catana.models.schemas.address import Address


class AddressRepository:
    """Address repository"""

    async def user_has_address(self, user_id: UUID):
        """If user has address in db return true"""
        user_id = db.session.query(AddressesInDb).filter_by(user_id=user_id).first()
        if user_id is None:
            return False
        return True

    async def delete_address(self, user_id: UUID):
        """Delete user address"""
        db.session.query(AddressesInDb).filter(
            AddressesInDb.user_id == user_id
        ).delete()

    async def add_address(self, address: Address, user_id: UUID):
        """Add user address"""
        address_db = AddressesInDb()
        address_db.user_id = user_id
        address_db.street = address.street
        address_db.local_no = address.local_no
        address_db.town = address.town
        address_db.postal_code = address.postal_code
        db.session.add(address_db)
        db.session.commit()
