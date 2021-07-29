"""Strings for HTTPException"""
from typing import Literal

USER_NAME_IS_EMPTY: Literal["Username is empty"]
EMAIL_IS_EMPTY: Literal["E-mail is empty"]
PASSWORD_IS_EMPTY: Literal["Password is empty"]
NAME_IS_EMPTY: Literal["Name is empty"]
SURNAME_IS_EMPTY: Literal["Surname is empty"]
PHONE_NUMBER_IS_EMPTY: Literal["Phone number is empty"]
USER_EMAIL_EXISTS: Literal["User email is exists"]
STREET_IS_EMPTY: Literal["Street is empty"]
LOCAL_NO_IS_EMPTY: Literal["Local number is empty"]
POSTAL_CODE_IS_EMPTY: Literal["Postal code is empty"]
TOWN_IS_EMPTY: Literal["Town is empty"]

USER_MAY_PROBABLY_DELETED = "User may probably deleted"
USER_NOT_EXISTS: Literal["User not exists"]

BOOK_ID_IS_EMPTY: Literal["Book ID is empty"]
USER_TOKEN_IS_EMPY: Literal["User token is empty"]

USER_HAS_BORROWED_BOOKS: Literal["User has borrowed books"]

INTERNAL_SERVER_ERROR: Literal["Internal server error"]
