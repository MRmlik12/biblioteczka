"""FastAPI events"""
from typing import Callable

from fastapi import FastAPI

from catana.db.events import close_db_connection, connect_to_db


def create_start_app_handler(app: FastAPI) -> Callable:
    """FastAPI start event"""

    async def start_app():
        await connect_to_db(app)

    return start_app


def create_stop_app_hadler(app: FastAPI) -> Callable:
    """FastAPI stop event"""

    async def stop_app():
        await close_db_connection(app)

    return stop_app
