"""About router"""
from fastapi.param_functions import Depends
from fastapi.params import Body
from fastapi.routing import APIRouter, HTTPException
from starlette.responses import JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST

from catana.api.dependencies.database import get_repository
from catana.assets import strings
from catana.db.repositories.user import UserRepository
from catana.models.schemas.users import UserInRegister

router = APIRouter()


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
    if user_register.name == "" or user_register.name == None:
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
    return JSONResponse({"created": True})
