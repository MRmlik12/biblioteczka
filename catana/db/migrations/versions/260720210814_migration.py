"""
26/07/2021 08:14
"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP

revision = "260720210814"
down_revision = None
branch_labels = "feature/user-address"
depends_on = None


def create_addresses_table() -> None:
    op.create_table(
        "addresses",
        sa.Column(
            "user_id", UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True
        ),
        sa.Column("street", sa.String, nullable=False, index=True),
        sa.Column("local_no", sa.String, nullable=False, index=True),
        sa.Column("town", sa.String, nullable=False, index=True),
        sa.Column("postal_code", sa.String, nullable=False, index=True),
        sa.Column("updated_at", TIMESTAMP, index=True, nullable=True),
    )
    op.execute(
        """
        CREATE TRIGGER update_address_modtime
            BEFORE UPDATE
            ON addresses
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """
    )


def upgrade() -> None:
    create_addresses_table()
