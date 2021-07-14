from pydantic import BaseModel
from pydantic.networks import EmailStr


class UserInRegister(BaseModel):
    email: EmailStr
    name: str
    surname: str
    password: str
    phone_number: str
