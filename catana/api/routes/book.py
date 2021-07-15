"""About router"""
from typing import List
from catana.db.repositories.user import UserRepository
from fastapi.param_functions import Body
from starlette.exceptions import HTTPException
from catana.db.repositories.book import BookRepository
from catana.models.schemas.books import Book, BookResponse, BoughtBook
from fastapi.params import Depends
from fastapi.routing import APIRouter
from catana.api.dependencies.database import get_repository
from catana.services.token import get_email_from_token


from starlette.responses import JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST
from catana.assets.strings import USER_TOKEN_IS_EMPY, BOOK_ID_IS_EMPTY

router = APIRouter()


@router.get("/list", response_model=List[Book])
async def book_list_router(
    books_repository: BookRepository = Depends(get_repository(BookRepository)),
) -> JSONResponse:
    books = await books_repository.get_books()
    return books


@router.post("/return")
async def return_book(
    book: BoughtBook = Body(..., embed=True),
    user_repository: UserRepository = Depends(get_repository(UserRepository)),
    books_repository: BookRepository = Depends(get_repository(BookRepository)),
) -> JSONResponse:
    user_id = await user_repository.get_user_id(get_email_from_token(book.token))
    await books_repository.return_book(user_id, book.id)
    return JSONResponse({"message": "ok"})


@router.post("/bought")
async def bought_book(
    book: BoughtBook = Body(..., embed=True),
    user_repository: UserRepository = Depends(get_repository(UserRepository)),
    books_repository: BookRepository = Depends(get_repository(BookRepository)),
) -> JSONResponse:
    if book.id == "":
        raise HTTPException(HTTP_400_BAD_REQUEST, BOOK_ID_IS_EMPTY)
    if book.token == "":
        raise HTTPException(HTTP_400_BAD_REQUEST, USER_TOKEN_IS_EMPY)
    user_id = await user_repository.get_user_id(get_email_from_token(book.token))
    await books_repository.assign_user(user_id, book.id)
    return JSONResponse({"message": "ok"})
