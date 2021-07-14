import asyncpg
from fastapi import FastAPI
from loguru import logger

from catana.core.config import POSTGRESQL_CONNECTION_STRING


async def connect_to_db(app: FastAPI):
    logger.info("Connecting to database")
    app.state.pool = await asyncpg.create_pool(POSTGRESQL_CONNECTION_STRING)
    logger.info("Connection established")


async def close_db_connection(app: FastAPI):
    await app.state.pool.close()
    logger.info("Connection closed")
