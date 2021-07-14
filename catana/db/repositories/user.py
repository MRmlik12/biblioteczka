from asyncpg import Connection

from catana.db.queries.queries import queries
from catana.db.repositories.base import BaseRepository
from catana.models.domain.users import UserInDb
from catana.models.schemas.users import UserInRegister


class UserRepository(BaseRepository):
    async def create_user(self, user_register: UserInRegister):
        user = UserInDb(user_register)
        user.create_password_hash(user_register.password)
        user.create_timestamp()
        user.generate_id()
        async with self.connection.transaction():
            await queries.create_user_account(
                self.connection,
                user.id,
                user.username,
                user.surname,
                user.email,
                user.salt,
                user.hashed_password,
                user.phone_number,
                user.date_created,
            )
