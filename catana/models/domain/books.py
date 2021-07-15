from uuid import UUID
from typing import Optional

class Book:
    id: UUID
    title: str
    autor: str
    isbn: str
    category: str
    publishing: str
    is_borrowed: bool
    user_borrow_id: Optional[UUID]


class BookInDb(Book):
    def assign_borrower(self, user_id: UUID):
        self.userBorrowID = user_id
