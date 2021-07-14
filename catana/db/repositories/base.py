from sqlalchemy import create_engine
from sqlalchemy.engine.base import Connection


class BaseRepository:
    def __init__(self, conn: Connection) -> None:
        self._conn = conn

    @property
    def connection(self) -> Connection:
        return self._conn
