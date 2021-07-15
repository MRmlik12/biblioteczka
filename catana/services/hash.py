import bcrypt
from passlib.context import CryptContext

context = CryptContext(schemes=["bcrypt"])


def generate_salt() -> str:
    return bcrypt.gensalt().decode()


def verify_hash(plain_content: str, hashed_content: str) -> bool:
    return context.verify(plain_content, hashed_content)


def get_hash(content: str) -> str:
    return context.hash(content)
