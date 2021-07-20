from uuid import UUID

from catana.db.queries.queries import queries
from catana.db.repositories.base import BaseRepository
from catana.models.schemas.books import Book


class BookRepository(BaseRepository):
    async def is_user_assigned(self, user_id: UUID) -> bool:
        count = await queries.select_user_borrows(self.connection, user_id)
        if count >= 1:
            return True
        return False

    async def return_book(self, user_id: UUID, book_id: UUID):
        await queries.return_book(self.connection, book_id, user_id)

    async def assign_user(self, user_id: UUID, book_id: UUID):
        await queries.assign_user(self.connection, user_id, book_id)

    async def get_book(self, book_id: UUID):
        book = await queries.get_book(self.connection, book_id)
        return Book(**book[0])

    async def get_books(self, page: int):
        offset = page * 10
        books = await queries.get_books(self.connection, offset)
        books_list = list()
        for book in books:
            books_list.append(Book(**book))
        return books_list
