"""User repository"""
from uuid import UUID

from catana.models.domain.users import User, UserInDb
from catana.models.schemas.users import UserInLogin, UserInRegister
from fastapi_sqlalchemy import db


class UserRepository:
    """User repository"""

    async def change_user_password(self, email: str, password: str):
        """Change user password"""
        user_db = UserInDb()
        user_db.create_password_hash(password)
        db.session.query(UserInDb).filter(UserInDb.email == email).update(
            {
                UserInDb.salt: user_db.salt,
                UserInDb.hashed_password: user_db.hashed_password,
            }
        )
        db.session.commit()

    async def delete_user(self, email: str):
        """Delete user by email"""
        print("XDD")
        user = UserInDb()
        user.email = email
        db.session.query(UserInDb).filter(UserInDb.email == email).delete()
        db.session.commit()

    async def get_user_id(self, email: str) -> UUID:
        """Get user id by email"""
        response = db.session.query(UserInDb).filter_by(email=email).first()
        return response.id

    async def login_user(self, user: UserInLogin) -> bool:
        """Login user"""
        user_credentials = (
            db.session.query(UserInDb).filter_by(email=user.email).first()
        )
        if user_credentials.check_password_hash(user.password):
            result = (
                db.session.query(UserInDb)
                .filter_by(hashed_password=user_credentials.hashed_password)
                .first()
            )
            if result.id != None:
                return True
        return False

    async def create_user(self, user_register: UserInRegister) -> bool:
        """create user, return True/False"""
        if (
            db.session.query(UserInDb).filter_by(email=user_register.email).first()
            == None
        ):
            user = UserInDb()
            user.create_password_hash(user_register.password)
            user.create_timestamp()
            user.generate_id()
            user.email = user_register.email
            user.phone_number = user_register.phone_number
            user.username = user_register.username
            user.surname = user_register.surname
            db.session.add(user)
            db.session.commit()
            return True
        return False
