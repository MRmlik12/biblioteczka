"""Book repository"""
from catana.models.domain.books import BookInDb
from uuid import UUID
from fastapi_sqlalchemy import db


class BookRepository:
    """Book repository"""

    async def is_user_not_assigned(self, user_id: UUID) -> bool:
        """Checks if user has borrowed book"""
        result = db.session.query(BookInDb).filter_by(user_borrow_id=user_id).first()
        if result == None:
            return True
        return False

    async def reassign_user(self, user_id: UUID, book_id: UUID, is_borrowed: bool):
        """Update information about book borrow status to true and insert user_id"""
        db.session.query(BookInDb).filter_by(id=book_id).update(
            {BookInDb.user_borrow_id: user_id, BookInDb.is_borrowed: is_borrowed}
        )
        db.session.commit()

    async def get_book(self, book_id: UUID):
        """Get book by id"""
        return db.session.query(BookInDb).filter_by(id=book_id).first()

    async def get_books(self, page: int):
        """Get books with pages"""
        offset = page * 10
        return db.session.query(BookInDb).offset(offset).limit(10).all()
