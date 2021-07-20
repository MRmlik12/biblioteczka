"""Token service"""
from datetime import datetime, timedelta

import jwt

from catana.core.config import JWT_SECRET_KEY
from catana.models.schemas.jwt import JWTUser

SUBJECT = "AUTH_TOKEN"
ALGORITHM = "HS512"
TOKEN_EXPIRE_IN_MINUTES = 60


def generate_token(email: str) -> str:
    """Generates JWT"""
    expires = datetime.utcnow() + timedelta(TOKEN_EXPIRE_IN_MINUTES)
    jwt_user = JWTUser(email=email, exp=expires, sub=SUBJECT)
    return jwt.encode(jwt_user.dict(), JWT_SECRET_KEY, ALGORITHM)


def get_email_from_token(token: str) -> str:
    """Try to get email from JWT"""
    try:
        decode = jwt.decode(token, JWT_SECRET_KEY, ALGORITHM)
        return decode["email"]
    except jwt.PyJWTError as jwt_error:
        raise ValueError("unable to decode JWT token") from jwt_error
