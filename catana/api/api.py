"""Main module to include routers"""
from fastapi import APIRouter

from catana.api.routes import about, book, user

router = APIRouter()
router.include_router(about.router, prefix="/about", tags=["index", "about"])
router.include_router(user.router, prefix="/user", tags=["login", "register"])
router.include_router(book.router, prefix="/book", tags=["list"])
