from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel


class Book(BaseModel):
    id: Optional[UUID]
    title: Optional[str]
    author: Optional[str]
    isbn: Optional[str]
    category: Optional[str]
    publishing: Optional[str]
    is_borrowed: Optional[bool]


class BoughtBook(BaseModel):
    id: UUID
    token: str


class BookResponse:
    books: List[Book]
