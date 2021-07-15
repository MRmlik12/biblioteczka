"""Main module"""
from fastapi import FastAPI
from fastapi.exceptions import HTTPException

from catana.api.errors.error import http_error_handler
from catana.api.api import router
from catana.core.events import create_start_app_handler, create_stop_app_hadler


def get_app() -> FastAPI:
    """Initialize FastAPI modules and return initialized modules"""
    app_init = FastAPI(title="Catana", debug=True, version=1)
    app_init.include_router(router, prefix="/api")

    app_init.add_exception_handler(HTTPException, http_error_handler)

    app_init.add_event_handler("startup", create_start_app_handler(app_init))
    app_init.add_event_handler("shutdown", create_stop_app_hadler(app_init))

    return app_init


app = get_app()
