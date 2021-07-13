"""Error module"""
from fastapi import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse


async def http_error_handler(_: Request, exc: HTTPException) -> JSONResponse:
    """Return JSON with raised errors"""
    return JSONResponse({"errors": [exc.detail]}, exc.status_code)
