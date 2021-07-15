"""
15/07/2021 11:09
"""
import uuid

import sqlalchemy as sa
from alembic import op
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID

revision = "150720211109"
down_revision = None
branch_labels = "feature/book-router"
depends_on = None


def create_users_table() -> None:
    op.create_table(
        "books",
        sa.Column(
            "id",
            UUID(as_uuid=True),
            nullable=False,
            primary_key=True,
            index=True,
            default=uuid.uuid4,
        ),
        sa.Column("title", sa.String, nullable=False, index=True),
        sa.Column("author", sa.String, nullable=False, index=True),
        sa.Column("isbn", sa.String, nullable=False, index=True),
        sa.Column("category", sa.String, nullable=False, index=True),
        sa.Column("publishing", sa.String, nullable=False, index=True),
        sa.Column("is_borrowed", sa.Boolean, nullable=False, index=True, default=False),
        sa.Column("user_borrow_id", UUID(as_uuid=True), index=True, nullable=True),
    )
    op.execute(
        """
        CREATE TRIGGER update_book_modtime
            BEFORE UPDATE
            ON books
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """
    )


def upgrade() -> None:
    create_users_table()
