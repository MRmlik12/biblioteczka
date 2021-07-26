"""Book router"""
from catana.db.repositories.address import AddressRepository
from uuid import UUID
from fastapi.param_functions import Body, Depends

from fastapi.routing import APIRouter
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST

from catana.assets import strings
from catana.db.repositories.book import BookRepository
from catana.db.repositories.user import UserRepository
from catana.models.schemas.books import BoughtBook
from catana.services.token import get_email_from_token

router = APIRouter()


@router.get("/list")
async def book_list(
    page: int,
    books_repository: BookRepository = Depends(BookRepository),
) -> JSONResponse:
    """Get list of books"""
    books = await books_repository.get_books(page)
    return books


@router.get("/{book_id}")
async def get_book_by_id(
    book_id: UUID,
    book_repository: BookRepository = Depends(BookRepository),
) -> JSONResponse:
    """Return book by id"""
    return await book_repository.get_book(book_id)


@router.post("/return")
async def return_book(
    book: BoughtBook = Body(..., embed=True),
    user_repository: UserRepository = Depends(UserRepository),
    books_repository: BookRepository = Depends(BookRepository),
    address_repository: AddressRepository = Depends(AddressRepository),
) -> JSONResponse:
    """Return borrowed book"""
    user_id = await user_repository.get_user_id(get_email_from_token(book.token))
    if address_repository.user_has_address(user_id):
        await books_repository.reassign_user(user_id, book.id, False)
    return JSONResponse({"message": "ok"})


@router.post("/bought")
async def bought_book(
    book: BoughtBook = Body(..., embed=True),
    user_repository: UserRepository = Depends(UserRepository),
    books_repository: BookRepository = Depends(BookRepository),
    address_repository: AddressRepository = Depends(AddressRepository),
) -> JSONResponse:
    """Assing user book"""
    if book.id == "":
        raise HTTPException(HTTP_400_BAD_REQUEST, strings.BOOK_ID_IS_EMPTY)
    if book.token == "":
        raise HTTPException(HTTP_400_BAD_REQUEST, strings.USER_TOKEN_IS_EMPY)
    user_id = await user_repository.get_user_id(get_email_from_token(book.token))
    if address_repository.user_has_address(user_id):
        await books_repository.reassign_user(user_id, book.id, True)
    return JSONResponse({"message": "ok"})
