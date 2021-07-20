"""Book repository"""
from uuid import UUID

from catana.db.queries.queries import queries
from catana.db.repositories.base import BaseRepository
from catana.models.schemas.books import Book


class BookRepository(BaseRepository):
    """Book repository"""

    async def is_user_not_assigned(self, user_id: UUID) -> bool:
        """Checks if user has borrowed book"""
        count = await queries.select_user_borrows(self.connection, user_id)
        if int(count[0]["count"]) == 0:
            return True
        return False

    async def return_book(self, user_id: UUID, book_id: UUID):
        """Update information about book borrow status to false and clear user_id"""
        await queries.return_book(self.connection, book_id, user_id)

    async def assign_user(self, user_id: UUID, book_id: UUID):
        """Update information about book borrow status to true and insert user_id"""
        await queries.assign_user(self.connection, user_id, book_id)

    async def get_book(self, book_id: UUID):
        """Get book by id"""
        book = await queries.get_book(self.connection, book_id)
        return Book(**book[0])

    async def get_books(self, page: int):
        """Get books with pages"""
        offset = page * 10
        books = await queries.get_books(self.connection, offset)
        books_list = list()
        for book in books:
            books_list.append(Book(**book))
        return books_list
