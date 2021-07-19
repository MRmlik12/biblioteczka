"""
14/07/2021 12:38
"""

import uuid

import sqlalchemy as sa
from alembic import op
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID

revision = "140720211238"
down_revision = None
branch_labels = "feature/book-router"
depends_on = None


def create_updated_at_trigger() -> None:
    op.execute(
        """
    CREATE FUNCTION update_updated_at_column()
        RETURNS TRIGGER AS
    $$
    BEGIN
        NEW.updated_at = now();
        RETURN NEW;
    END;
    $$ language 'plpgsql';
    """
    )


def create_users_table() -> None:
    op.create_table(
        "users",
        sa.Column(
            "id",
            UUID(as_uuid=True),
            nullable=False,
            primary_key=True,
            index=True,
            default=uuid.uuid4,
        ),
        sa.Column("username", sa.String, nullable=False),
        sa.Column("surname", sa.String, nullable=False),
        sa.Column("email", sa.String, nullable=False, index=True),
        sa.Column("salt", sa.String, nullable=False),
        sa.Column("hashed_password", sa.String, nullable=False),
        sa.Column("phone_number", sa.String, nullable=False),
        sa.Column("created_at", sa.TIMESTAMP, nullable=False),
    )
    op.execute(
        """
        CREATE TRIGGER update_user_modtime
            BEFORE UPDATE
            ON users
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """
    )


def upgrade() -> None:
    create_updated_at_trigger()
    create_users_table()
