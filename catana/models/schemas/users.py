"""Users schema"""
from pydantic import BaseModel
from pydantic.networks import EmailStr


class UserAuth(BaseModel):
    """UserAuth schema"""

    token: str


class UserInResetPassword(UserAuth):
    """UserInResetPassword schema"""

    password: str


class UserInLogin(BaseModel):
    """UserInLogin schema"""

    email: EmailStr
    password: str


class UserInRegister(UserInLogin):
    """UserInRegister schema"""

    username: str
    surname: str
    phone_number: str
