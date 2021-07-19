from uuid import UUID

from catana.db.queries.queries import queries
from catana.db.repositories.base import BaseRepository
from catana.models.domain.users import UserInDb
from catana.models.schemas.users import UserInLogin, UserInRegister


class UserRepository(BaseRepository):
    async def get_user_id(self, email: str) -> UUID:
        response = await queries.get_user_id(self.connection, email)
        print(response)
        return response[0]["id"]

    async def get_user(self, user: UserInLogin) -> bool:
        user_credentials = await queries.get_user_login_credentials(
            self.connection, user.email
        )
        user_db = UserInDb()
        user_db.hashed_password = user_credentials[0]["hashed_password"]
        user_db.salt = user_credentials[0]["salt"]
        return user_db.check_password_hash(user.password)

    async def create_user(self, user_register: UserInRegister):
        user = UserInDb()
        user.create_password_hash(user_register.password)
        user.create_timestamp()
        user.generate_id()
        async with self.connection.transaction():
            await queries.create_user_account(
                self.connection,
                user.id,
                user_register.username,
                user_register.surname,
                user_register.email,
                user.salt,
                user.hashed_password,
                user_register.phone_number,
                user.date_created,
            )
