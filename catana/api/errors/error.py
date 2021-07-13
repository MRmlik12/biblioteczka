from fastapi import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse, Response


async def http_error_handler(_: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse({"errors": [exc.detail]}, exc.status_code)
