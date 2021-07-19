import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from starlette.status import HTTP_200_OK
from catana.services.token import generate_token
import json

pytestmark = pytest.mark.asyncio


async def test_book_list_check_status_code_is_OK(app: FastAPI, client: AsyncClient):
    response = await client.request(method="GET", url=app.url_path_for("book_list"))
    assert response.status_code == HTTP_200_OK


async def test_get_book_by_id_checks_status_code_is_OK(
    app: FastAPI, client: AsyncClient
):
    response = await client.request(
        method="GET",
        url="/api/book/1b5ffaca-1623-44f5-a055-41a01feaaf9d",
    )
    assert response.status_code == HTTP_200_OK


async def test_bought_book_check_status_code_is_OK(app: FastAPI, client: AsyncClient):
    book = {
        "book": {
            "id": "1b5ffaca-1623-44f5-a055-41a01feaaf9d",
            "token": generate_token("jan@kowalski.com"),
        }
    }
    response = await client.request(
        method="POST", url=app.url_path_for("bought_book"), content=json.dumps(book)
    )
    assert response.status_code == HTTP_200_OK

async def test_return_book_check_status_code_is_OK(app: FastAPI, client: AsyncClient):
    book = {
        "book": {
            "id": "1b5ffaca-1623-44f5-a055-41a01feaaf9d",
            "token": generate_token("jan@kowalski.com"),
        }
    }
    response = await client.request(
        method="POST", url=app.url_path_for("bought_book"), content=json.dumps(book)
    )
    assert response.status_code == HTTP_200_OK
