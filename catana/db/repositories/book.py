from catana.api.routes import user
from catana.models.domain.books import BookInDb
from os import O_NOINHERIT
from uuid import UUID
from typing import List
from catana.models.schemas.books import Book
from catana.db.repositories.base import BaseRepository
from catana.db.queries.queries import queries


class BookRepository(BaseRepository):
    async def return_book(self, user_id: UUID, book_id: UUID):
        await queries.return_book(self.connection, book_id, user_id)

    async def assign_user(self, user_id: UUID, book_id: UUID):
        await queries.assign_user(self.connection, user_id, book_id)

    async def get_book(self, book_id: UUID):
        book = await queries.get_book(self.connection, book_id)
        return Book(**book[0])

    async def get_books(self):
        books = await queries.get_books(self.connection)
        books_list = list()
        for book in books:
            books_list.append(Book(**book))
        return books_list
