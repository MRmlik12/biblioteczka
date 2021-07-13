from typing import Optional

from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from catana.api.routes.api import router
from catana.api.errors.error import http_error_handler

app = FastAPI()


def get_app() -> FastAPI:
    app = FastAPI(title="Catana", debug=True, version=1)
    app.include_router(router, prefix="/api")
    app.add_exception_handler(HTTPException, http_error_handler)

    return app


app = get_app()
