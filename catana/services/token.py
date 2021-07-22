"""Token service"""
from datetime import datetime, timedelta
from typing import Literal

import jwt

from catana.core.config import JWT_SECRET_KEY
from catana.models.schemas.jwt import JWTUser

SUBJECT: Literal["AUTH_TOKEN"]
ALGORITHM: Literal["HS512"]
TOKEN_EXPIRE_IN_MINUTES: Literal[60]


def generate_token(email: str) -> str:
    """Generates JWT"""
    expires = datetime.utcnow() + timedelta(TOKEN_EXPIRE_IN_MINUTES)
    jwt_user = JWTUser(email=email, exp=expires, sub=SUBJECT)
    return jwt.encode(jwt_user.dict(), str(JWT_SECRET_KEY), ALGORITHM)


def get_email_from_token(token: str) -> str:
    """Try to get email from JWT"""
    try:
        decode = jwt.decode(token, str(JWT_SECRET_KEY), list(ALGORITHM))
        return decode["email"]
    except jwt.PyJWTError as jwt_error:
        raise ValueError("unable to decode JWT token") from jwt_error
