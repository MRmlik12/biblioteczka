"""Books domain"""
from uuid import uuid4
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Boolean, String, TIMESTAMP
from catana.models.domain.base import Base
from sqlalchemy.dialects.postgresql import UUID


class Book(Base):
    """Book entity"""

    __tablename__ = "books"
    id = Column("id", (UUID(as_uuid=True)), primary_key=True, default=uuid4)
    title = Column("title", String, nullable=False)
    author = Column("author", String, nullable=False)
    isbn = Column("isbn", String, nullable=False)
    category = Column("category", String, nullable=False)
    publishing = Column("publishing", String, nullable=False)
    is_borrowed = Column("is_borrowed", Boolean, nullable=False, default=False)
    user_borrow_id = Column("user_borrow_id", (UUID(as_uuid=True)), nullable=True)
    updated_at = Column("updated_at", TIMESTAMP, nullable=True)


class BookInDb(Book):
    """Book db operations"""

    pass
