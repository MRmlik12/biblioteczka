"""User router"""
from fastapi.param_functions import Body, Depends
from fastapi.routing import APIRouter, HTTPException
from starlette.responses import JSONResponse
from starlette.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_406_NOT_ACCEPTABLE,
    HTTP_500_INTERNAL_SERVER_ERROR,
)

from catana.assets import strings
from catana.db.repositories.address import AddressRepository
from catana.db.repositories.book import BookRepository
from catana.db.repositories.user import UserRepository
from catana.models.schemas.address import Address
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
    user_repository: UserRepository = Depends(UserRepository),
) -> JSONResponse:
    """Login endpoint"""
    user = await user_repository.login_user(user_login)
    if user:
        return JSONResponse({"token": generate_token(user_login.email)})
    raise HTTPException(HTTP_401_UNAUTHORIZED, "Wrong login credentials")


@router.post("/register")
async def register_user(
    user_register: UserInRegister = Body(..., embed=True),
    user_repository: UserRepository = Depends(UserRepository),
) -> JSONResponse:
    """Register new user"""
    if user_register.email == "":
        raise HTTPException(HTTP_400_BAD_REQUEST, strings.EMAIL_IS_EMPTY)
    if user_register.password == "":
        raise HTTPException(HTTP_400_BAD_REQUEST, strings.PASSWORD_IS_EMPTY)
    if user_register.username == "":
        raise HTTPException(HTTP_400_BAD_REQUEST, strings.NAME_IS_EMPTY)
    if user_register.surname == "":
        raise HTTPException(HTTP_400_BAD_REQUEST, strings.PASSWORD_IS_EMPTY)
    if user_register.phone_number == "":
        raise HTTPException(HTTP_400_BAD_REQUEST, strings.PASSWORD_IS_EMPTY)
    if await user_repository.create_user(user_register):
        return JSONResponse({"token": generate_token(user_register.email)})
    raise HTTPException(HTTP_400_BAD_REQUEST, strings.USER_EMAIL_EXISTS)


@router.put("/resetPassword")
async def reset_password(
    user_auth: UserInResetPassword = Body(..., embed=True),
    user_repository: UserRepository = Depends(UserRepository),
) -> None:
    """Reset password for actual user"""
    try:
        await user_repository.change_user_password(
            get_email_from_token(user_auth.token), user_auth.password
        )
    except Exception as exception:
        raise HTTPException(
            HTTP_500_INTERNAL_SERVER_ERROR, "error in resetting password"
        ) from exception


@router.delete("/delete")
async def delete_user(
    user_delete: UserAuth = Body(..., embed=True),
    user_repository: UserRepository = Depends(UserRepository),
    book_repository: BookRepository = Depends(BookRepository),
    address_repository: AddressRepository = Depends(AddressRepository),
) -> None:
    """Reset password for acctual user"""
    try:
        email = get_email_from_token(user_delete.token)
        user = await user_repository.get_user_id(email)
        if await book_repository.is_user_not_assigned(user):
            await address_repository.delete_address(user)
            await user_repository.delete_user(email)
            return
        raise HTTPException(HTTP_406_NOT_ACCEPTABLE, strings.USER_HAS_BORROWED_BOOKS)
    except IndexError as index_error:
        raise HTTPException(
            HTTP_500_INTERNAL_SERVER_ERROR, "user may probably deleted"
        ) from index_error


@router.post("/setAddress")
async def set_address(
    user_address: Address = Body(..., embed=True),
    user_repository: UserRepository = Depends(UserRepository),
    address_repository: AddressRepository = Depends(AddressRepository),
):
    """Set new address for user"""
    try:
        if user_address.street == "":
            raise HTTPException(HTTP_400_BAD_REQUEST, strings.STREET_IS_EMPTY)
        if user_address.local_no == "":
            raise HTTPException(HTTP_400_BAD_REQUEST, strings.LOCAL_NO_IS_EMPTY)
        if user_address.town == "":
            raise HTTPException(HTTP_400_BAD_REQUEST, strings.TOWN_IS_EMPTY)
        if user_address.postal_code == "":
            raise HTTPException(HTTP_400_BAD_REQUEST, strings.POSTAL_CODE_IS_EMPTY)
        user_id = await user_repository.get_user_id(
            get_email_from_token(user_address.token)
        )
        address_repository.add_address(user_address, user_id)
    except Exception as address_exception:
        raise HTTPException(
            HTTP_500_INTERNAL_SERVER_ERROR, "Internal server error"
        ) from address_exception
