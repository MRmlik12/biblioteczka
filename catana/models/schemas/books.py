"""Book schemas"""
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


class Book(BaseModel):
    """Book vase schema"""

    id: Optional[UUID]
    title: Optional[str]
    author: Optional[str]
    isbn: Optional[str]
    category: Optional[str]
    publishing: Optional[str]
    is_borrowed: Optional[bool]


class BoughtBook(BaseModel):
    """Bought book"""

    id: UUID
    token: str


class BookResponse:
    """Response book list"""

    books: List[Book]
