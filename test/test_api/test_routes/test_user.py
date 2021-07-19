from fastapi.param_functions import Body
import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from starlette.status import HTTP_200_OK
import json

pytestmark = pytest.mark.asyncio


async def test_user_register_check_status_code_is_OK(app: FastAPI, client: AsyncClient):
    user = {
        "user_register": {
            "username": "Jan",
            "surname": "Kowalski",
            "email": "jan@kowalski.com",
            "password": "test",
            "phone_number": "100-100-100",
        }
    }
    response = await client.request(
        method="POST", url=app.url_path_for("register_user"), content=json.dumps(user)
    )
    assert response.status_code == HTTP_200_OK


async def test_user_login_cheks_status_code_is_OK(app: FastAPI, client: AsyncClient):
    login = {"user_login": {"email": "jan@kowalski.com", "password": "test"}}
    response = await client.request(
        method="POST", url=app.url_path_for("login_user"), content=json.dumps(login)
    )
    assert response.status_code == HTTP_200_OK
