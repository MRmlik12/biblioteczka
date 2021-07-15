from catana.models.schemas.jwt import JWTUser
from datetime import datetime, timedelta
from catana.core.config import JWT_SECRET_KEY
import jwt

SUBJECT = "AUTH_TOKEN"
ALGORITHM = "HS512"
TOKEN_EXPIRE_IN_MINUTES = 60


def generate_token(email: str) -> str:
    expires = datetime.utcnow() + timedelta(TOKEN_EXPIRE_IN_MINUTES)
    jwt_user = JWTUser(email=email, exp=expires, sub=SUBJECT)
    return jwt.encode(jwt_user.dict(), JWT_SECRET_KEY, ALGORITHM)


def get_email_from_token(token: str) -> str:
    try:
        decode = jwt.decode(token, JWT_SECRET_KEY, ALGORITHM)
        return decode["email"]
    except jwt.PyJWTError:
        raise ValueError("unable to decode JWT token")
