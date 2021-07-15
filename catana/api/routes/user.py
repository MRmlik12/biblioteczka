"""About router"""
from fastapi.param_functions import Depends
from fastapi.params import Body
from fastapi.routing import APIRouter, HTTPException
from starlette.responses import JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED

from catana.api.dependencies.database import get_repository
from catana.assets import strings
from catana.db.repositories.user import UserRepository
from catana.models.schemas.users import UserInLogin, UserInRegister
from catana.services.token import generate_token, get_email_from_token

router = APIRouter()


@router.post("/login")
async def login_user(
    user_login: UserInLogin = Body(..., embed=True),
    user_repository: UserRepository = Depends(get_repository(UserRepository)),
) -> JSONResponse:
    user = await user_repository.get_user(user_login)
    if user:
        return JSONResponse({"token": generate_token(user_login.email)})
    raise HTTPException(HTTP_401_UNAUTHORIZED, "Wrong login credentials")


@router.post("/register")
async def register_user(
    user_register: UserInRegister = Body(..., embed=True),
    user_repository: UserRepository = Depends(get_repository(UserRepository)),
) -> JSONResponse:
    if user_register.email == "" or user_register.email == None:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail=strings.EMAIL_IS_EMPTY
        )
    if user_register.password == "" or user_register.password == None:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail=strings.PASSWORD_IS_EMPTY
        )
    if user_register.username == "" or user_register.username == None:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail=strings.NAME_IS_EMPTY
        )
    if user_register.surname == "" or user_register.surname == None:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail=strings.PASSWORD_IS_EMPTY
        )
    if user_register.phone_number == "" or user_register.phone_number == None:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail=strings.PASSWORD_IS_EMPTY
        )
    await user_repository.create_user(user_register)
    return JSONResponse({"token": generate_token(user_register.email)})
