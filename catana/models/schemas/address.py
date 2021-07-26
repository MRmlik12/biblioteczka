"""Address"""
from pydantic.main import BaseModel


class Address(BaseModel):
    """Address schema"""

    token: str
    street: str
    local_no: str
    town: str
    postal_code: str
