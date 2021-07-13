"""Main module"""
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from catana.api.routes.api import router
from catana.api.errors.error import http_error_handler


def get_app() -> FastAPI:
    """Initialize FastAPI modules and return initialized modules"""
    app_init = FastAPI(title="Catana", debug=True, version=1)
    app_init.include_router(router, prefix="/api")
    app_init.add_exception_handler(HTTPException, http_error_handler)

    return app_init


app = get_app()
