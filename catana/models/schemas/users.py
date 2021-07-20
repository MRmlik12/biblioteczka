from pydantic import BaseModel
from pydantic.networks import EmailStr


class UserAuth(BaseModel):
    token: str


class UserInResetPassword(UserAuth):
    password: str


class UserInLogin(BaseModel):
    email: EmailStr
    password: str


class UserInRegister(UserInLogin):
    username: str
    surname: str
    phone_number: str
