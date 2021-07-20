"""Base repository"""
from sqlalchemy.engine.base import Connection


class BaseRepository:
    """BaseRepository class"""

    def __init__(self, conn: Connection) -> None:
        self._conn = conn

    @property
    def connection(self) -> Connection:
        """asyncpg connection"""
        return self._conn
