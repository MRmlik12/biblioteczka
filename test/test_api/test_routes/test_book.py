import json
from uuid import UUID

import pytest
import sqlalchemy
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy.sql.expression import table
from starlette.status import HTTP_200_OK

from catana.core.config import POSTGRESQL_CONNECTION_STRING
from catana.services.token import generate_token

pytestmark = pytest.mark.asyncio


engine = sqlalchemy.create_engine(POSTGRESQL_CONNECTION_STRING).connect()
engine.execute(
    sqlalchemy.text(
        """
    INSERT INTO books(id, title, author, isbn, category, publishing, is_borrowed, user_borrow_id, updated_at) 
    VALUES ('1b5ccaca-1623-44f5-a055-41a01feaaf9d', 'Pan Tadeusz', 'Adam Mickiewicz', '9788304004467', 'Poetry', 'Hippocrene Books', FALSE, NULL, NULL);
    """
    )
)
engine.execute(
    sqlalchemy.text(
        """
    INSERT INTO books(id, title, author, isbn, category, publishing, is_borrowed, user_borrow_id, updated_at) 
    VALUES ('1b5cca14-1623-44f5-a055-41a01feaaf9d', 'Makbet', 'William Shakespear', '9788304004467', 'Tragedy', 'Hippocrene Books', FALSE, NULL, NULL);
    """
    )
)

token = generate_token("jan@kowalski.pl")


async def test_create_test_user(app: FastAPI, client: AsyncClient):
    user = {
        "user_register": {
            "username": "Jan",
            "surname": "Kow",
            "email": "jan@kowalski.pl",
            "password": "test",
            "phone_number": "101-100-100",
        }
    }
    await client.request(
        method="POST", url=app.url_path_for("register_user"), content=json.dumps(user)
    )


async def test_book_list_check_status_code_is_OK(app: FastAPI, client: AsyncClient):
    response = await client.request(
        method="GET", url=app.url_path_for("book_list"), params={"page": 0}
    )
    assert response.status_code == HTTP_200_OK


async def test_get_book_by_id_checks_status_code_is_OK(client: AsyncClient):
    response = await client.request(
        method="GET",
        url="/api/book/1b5ccaca-1623-44f5-a055-41a01feaaf9d",
    )
    assert response.status_code == HTTP_200_OK


async def test_bought_book_check_status_code_is_OK(app: FastAPI, client: AsyncClient):
    book = {
        "book": {
            "id": "1b5ccaca-1623-44f5-a055-41a01feaaf9d",
            "token": generate_token("jan@kowalski.pl"),
        }
    }
    response = await client.request(
        method="PUT", url=app.url_path_for("bought_book"), content=json.dumps(book)
    )
    assert response.status_code == HTTP_200_OK


async def test_return_book_check_status_code_is_OK(app: FastAPI, client: AsyncClient):
    book = {
        "book": {
            "id": "1b5ccaca-1623-44f5-a055-41a01feaaf9d",
            "token": generate_token("jan@kowalski.pl"),
        }
    }
    response = await client.request(
        method="PUT", url=app.url_path_for("bought_book"), content=json.dumps(book)
    )
    assert response.status_code == HTTP_200_OK
