"""Hash service"""
import bcrypt
from passlib.context import CryptContext

context = CryptContext(schemes=["bcrypt"])


def generate_salt() -> str:
    """Generate salt to hash password"""
    return bcrypt.gensalt().decode()


def verify_hash(plain_content: str, hashed_content: str) -> bool:
    """Cheks if user password is correct"""
    return context.verify(plain_content, hashed_content)


def get_hash(content: str) -> str:
    """Get hashed password"""
    return context.hash(content)
