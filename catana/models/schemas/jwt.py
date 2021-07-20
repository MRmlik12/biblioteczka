"""JWT schema"""
from datetime import datetime

from pydantic import BaseModel


class JWTMeta(BaseModel):
    """Meta class to keep token subject and expire time"""

    exp: datetime
    sub: str


class JWTUser(JWTMeta):
    """User credentials"""

    email: str
