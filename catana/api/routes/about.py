"""About router"""
from fastapi.routing import APIRouter
from starlette.responses import JSONResponse

router = APIRouter()


@router.get("")
async def index_router() -> JSONResponse:
    """Return API version code"""
    return JSONResponse({"version": 1})
