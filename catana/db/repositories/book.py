"""Book repository"""
from typing import Optional
from uuid import UUID

from fastapi_sqlalchemy import db

from catana.models.domain.books import BookInDb


class BookRepository:
    """Book repository"""

    async def is_user_not_assigned(self, user_id: UUID) -> bool:
        """Checks if user has borrowed book"""
        result = db.session.query(BookInDb).filter_by(user_borrow_id=user_id).first()
        if result is None:
            return True
        return False

    async def reassign_user(
        self, user_id: Optional[UUID], book_id: UUID, is_borrowed: bool
    ) -> None:
        """Update information about book borrow status to true and insert user_id"""
        db.session.query(BookInDb).filter_by(id=book_id).update(
            {BookInDb.user_borrow_id: user_id, BookInDb.is_borrowed: is_borrowed}
        )
        db.session.commit()

    async def get_book(self, book_id: UUID) -> BookInDb:
        """Get book by id"""
        return db.session.query(BookInDb).filter_by(id=book_id).first()

    async def get_books(self, page: int) -> BookInDb:
        """Get books with pages"""
        offset = page * 10
        return db.session.query(BookInDb).offset(offset).limit(10).all()
