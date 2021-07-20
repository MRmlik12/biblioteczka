"""User router"""
from fastapi.param_functions import Depends
from fastapi.params import Body
from fastapi.routing import APIRouter, HTTPException
from starlette.responses import JSONResponse
from starlette.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_406_NOT_ACCEPTABLE,
    HTTP_500_INTERNAL_SERVER_ERROR,
)

from catana.api.dependencies.database import get_repository
from catana.assets import strings
from catana.db.repositories.book import BookRepository
from catana.db.repositories.user import UserRepository
from catana.models.schemas.users import (
    UserAuth,
    UserInLogin,
    UserInRegister,
    UserInResetPassword,
)
from catana.services.token import generate_token, get_email_from_token

router = APIRouter()


@router.post("/login")
async def login_user(
    user_login: UserInLogin = Body(..., embed=True),
    user_repository: UserRepository = Depends(get_repository(UserRepository)),
) -> JSONResponse:
    """Login endpoint"""
    user = await user_repository.login_user(user_login)
    print(user)
    if user:
        return JSONResponse({"token": generate_token(user_login.email)})
    raise HTTPException(HTTP_401_UNAUTHORIZED, "Wrong login credentials")


@router.post("/register")
async def register_user(
    user_register: UserInRegister = Body(..., embed=True),
    user_repository: UserRepository = Depends(get_repository(UserRepository)),
) -> JSONResponse:
    """Register new user"""
    if user_register.email == "" | user_register.email == None:
        raise HTTPException(HTTP_400_BAD_REQUEST, strings.EMAIL_IS_EMPTY)
    if user_register.password == "" | user_register.password == None:
        raise HTTPException(HTTP_400_BAD_REQUEST, strings.PASSWORD_IS_EMPTY)
    if user_register.username == "" | user_register.username == None:
        raise HTTPException(HTTP_400_BAD_REQUEST, strings.NAME_IS_EMPTY)
    if user_register.surname == "" | user_register.surname == None:
        raise HTTPException(HTTP_400_BAD_REQUEST, strings.PASSWORD_IS_EMPTY)
    if user_register.phone_number == "" | user_register.phone_number == None:
        raise HTTPException(HTTP_400_BAD_REQUEST, strings.PASSWORD_IS_EMPTY)
    if await user_repository.create_user(user_register):
        return JSONResponse({"token": generate_token(user_register.email)})
    raise HTTPException(HTTP_400_BAD_REQUEST, strings.USER_EMAIL_EXISTS)


@router.put("/resetPassowrd")
async def reset_password(
    user_auth: UserInResetPassword = Body(..., embed=True),
    user_repository: UserRepository = Depends(get_repository(UserRepository)),
) -> JSONResponse:
    """Reset password for acctual user"""
    try:
        user_repository.change_user_password(
            get_email_from_token(user_auth.token), user_auth.password
        )
    except Exception as exception:
        raise HTTPException(
            HTTP_500_INTERNAL_SERVER_ERROR, "error in resetting password"
        ) from exception


@router.delete("/delete")
async def delete_user(
    user_delete: UserAuth = Body(..., embed=True),
    user_repository: UserRepository = Depends(get_repository(UserRepository)),
    book_repository: BookRepository = Depends(get_repository(BookRepository)),
) -> JSONResponse:
    """Reset password for acctual user"""
    try:
        email = get_email_from_token(user_delete.token)
        user = await user_repository.get_user_id(email)
        if book_repository.is_user_assigned(user):
            await user_repository.delete_user(email)
        raise HTTPException(HTTP_406_NOT_ACCEPTABLE, strings.USER_HAS_BORROWED_BOOKS)
    except IndexError as index_error:
        raise HTTPException(
            HTTP_500_INTERNAL_SERVER_ERROR, "user may probably deleted"
        ) from index_error
