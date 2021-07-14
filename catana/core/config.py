from starlette import config
from starlette.config import Config

conf = Config(".env")
POSTGRESQL_CONNECTION_STRING = conf("POSTGRES_CONNECTION_STRING")
