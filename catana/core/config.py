import os

from starlette import config
from starlette.config import Config

conf = Config(".env")
POSTGRESQL_CONNECTION_STRING = "postgresql://test:123@localhost:5432/catana_db"
JWT_SECRET_KEY = "OPdNtRVFv/lJ+sPQyvy/UDoPe4w3cE4Ld8DKWXK1hLGOoKzfyWkDVdqmwuGT2dbwyrSp5i9HOifgoKpRDpV5kg=="
