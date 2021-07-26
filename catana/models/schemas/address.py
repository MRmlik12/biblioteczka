from uuid import UUID

from pydantic.main import BaseModel


class Address(BaseModel):
    token: str
    street: str
    local_no: str
    town: str
    postal_code: str
