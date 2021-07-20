"""Books domain"""
from typing import Optional
from uuid import UUID


class Book:
    """Book entity"""

    id: UUID
    title: str
    autor: str
    isbn: str
    category: str
    publishing: str
    is_borrowed: bool
    user_borrow_id: Optional[UUID]


class BookInDb(Book):
    """Book db operations"""

    pass
