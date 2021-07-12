from fastapi import APIRouter
from catana.api.routes import about

router = APIRouter()
router.include_router(about.router, prefix="/about", tags=["index", "about"])
