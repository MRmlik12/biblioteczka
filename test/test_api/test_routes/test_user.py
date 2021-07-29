import json

import pytest
from fastapi import FastAPI
from fastapi.param_functions import Body
from httpx import AsyncClient
from starlette.status import (
    HTTP_200_OK,
    HTTP_202_ACCEPTED,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_406_NOT_ACCEPTABLE,
    HTTP_422_UNPROCESSABLE_ENTITY,
    HTTP_500_INTERNAL_SERVER_ERROR,
)

from catana.services.token import generate_token

pytestmark = pytest.mark.asyncio


token = generate_token("jan@kowalski.com")


async def test_user_register_check_status_code_is_OK(app: FastAPI, client: AsyncClient):
    user = {
        "user_register": {
            "username": "Jan",
            "surname": "Kowalski",
            "email": "jan@kowalski.com",
            "password": "123",
            "phone_number": "100-100-100",
        }
    }
    response = await client.request(
        method="POST", url=app.url_path_for("register_user"), content=json.dumps(user)
    )
    assert response.status_code == HTTP_200_OK


async def test_user_register_check_status_code_is_400_when_username_empty(
    app: FastAPI, client: AsyncClient
):
    user = {
        "user_register": {
            "username": "",
            "surname": "Kowalski",
            "email": "jan@kowalski.com",
            "password": "123",
            "phone_number": "100-100-100",
        }
    }
    response = await client.request(
        method="POST", url=app.url_path_for("register_user"), content=json.dumps(user)
    )
    assert response.status_code == HTTP_400_BAD_REQUEST


async def test_user_register_check_status_code_is_400_when_surname_empty(
    app: FastAPI, client: AsyncClient
):
    user = {
        "user_register": {
            "username": "Jan",
            "surname": "",
            "email": "jan@kowalski.com",
            "password": "123",
            "phone_number": "100-100-100",
        }
    }
    response = await client.request(
        method="POST", url=app.url_path_for("register_user"), content=json.dumps(user)
    )
    assert response.status_code == HTTP_400_BAD_REQUEST


async def test_user_register_check_status_code_is_400_when_email_empty(
    app: FastAPI, client: AsyncClient
):
    user = {
        "user_register": {
            "username": "Jan",
            "surname": "Kowalski",
            "email": "",
            "password": "123",
            "phone_number": "100-100-100",
        }
    }
    response = await client.request(
        method="POST", url=app.url_path_for("register_user"), content=json.dumps(user)
    )
    assert response.status_code == HTTP_422_UNPROCESSABLE_ENTITY


async def test_user_register_check_status_code_is_400_when_password_empty(
    app: FastAPI, client: AsyncClient
):
    user = {
        "user_register": {
            "username": "Jan",
            "surname": "Kowalski",
            "email": "jan@kowalski.com",
            "password": "",
            "phone_number": "100-100-100",
        }
    }
    response = await client.request(
        method="POST", url=app.url_path_for("register_user"), content=json.dumps(user)
    )
    assert response.status_code == HTTP_400_BAD_REQUEST


async def test_user_register_check_status_code_is_400_when_surnmae_empty(
    app: FastAPI, client: AsyncClient
):
    user = {
        "user_register": {
            "username": "Jan",
            "surname": "Kowalski",
            "email": "jan@kowalski.com",
            "password": "123",
            "phone_number": "",
        }
    }
    response = await client.request(
        method="POST", url=app.url_path_for("register_user"), content=json.dumps(user)
    )
    assert response.status_code == HTTP_400_BAD_REQUEST


async def test_user_login_cheks_status_code_is_OK(app: FastAPI, client: AsyncClient):
    login = {"user_login": {"email": "jan@kowalski.com", "password": "123"}}
    response = await client.request(
        method="POST", url=app.url_path_for("login_user"), content=json.dumps(login)
    )
    assert response.status_code == HTTP_200_OK


async def test_user_reset_password_cheks_status_code_is_OK(
    app: FastAPI, client: AsyncClient
):
    reset = {"user_auth": {"token": token, "password": "123"}}
    response = await client.request(
        method="PUT", url=app.url_path_for("reset_password"), content=json.dumps(reset)
    )
    assert response.status_code == HTTP_200_OK


async def test_user_set_address_checks_status_code_is_OK(
    app: FastAPI, client: AsyncClient
):
    set_address = {
        "user_address": {
            "token": token,
            "street": "Kowalski",
            "local_no": "4",
            "town": "Warsaw",
            "postal_code": "99-999",
        }
    }
    response = response = await client.request(
        method="POST",
        url=app.url_path_for("set_address"),
        content=json.dumps(set_address),
    )
    assert response.status_code == HTTP_200_OK


async def test_user_set_address_checks_status_code_is_400_street_empty(
    app: FastAPI, client: AsyncClient
):
    set_address = {
        "user_address": {
            "token": token,
            "street": "",
            "local_no": "4",
            "town": "Warsaw",
            "postal_code": "99-999",
        }
    }
    response = response = await client.request(
        method="POST",
        url=app.url_path_for("set_address"),
        content=json.dumps(set_address),
    )
    assert response.status_code == HTTP_400_BAD_REQUEST


async def test_user_set_address_checks_status_code_is_400_local_no_empty(
    app: FastAPI, client: AsyncClient
):
    set_address = {
        "user_address": {
            "token": token,
            "street": "XXX",
            "local_no": "",
            "town": "Warsaw",
            "postal_code": "99-999",
        }
    }
    response = response = await client.request(
        method="POST",
        url=app.url_path_for("set_address"),
        content=json.dumps(set_address),
    )
    assert response.status_code == HTTP_400_BAD_REQUEST


async def test_user_set_address_checks_status_code_is_400_town_empty(
    app: FastAPI, client: AsyncClient
):
    set_address = {
        "user_address": {
            "token": token,
            "street": "XXX",
            "local_no": "XX",
            "town": "",
            "postal_code": "99-999",
        }
    }
    response = response = await client.request(
        method="POST",
        url=app.url_path_for("set_address"),
        content=json.dumps(set_address),
    )
    assert response.status_code == HTTP_400_BAD_REQUEST


async def test_user_set_address_checks_status_code_is_400_postal_code_empty(
    app: FastAPI, client: AsyncClient
):
    set_address = {
        "user_address": {
            "token": token,
            "street": "XXX",
            "local_no": "XX",
            "town": "XXX",
            "postal_code": "",
        }
    }
    response = response = await client.request(
        method="POST",
        url=app.url_path_for("set_address"),
        content=json.dumps(set_address),
    )
    assert response.status_code == HTTP_400_BAD_REQUEST


async def test_user_delete_checks_status_code_is_OK(app: FastAPI, client: AsyncClient):
    delete = {"user_delete": {"token": token}}
    response = response = await client.request(
        method="DELETE",
        url=app.url_path_for("delete_user"),
        content=json.dumps(delete),
    )
    assert response.status_code == HTTP_200_OK


async def test_user_delete_throw_HTTP_EXCEPTION(app: FastAPI, client: AsyncClient):
    delete = {"user_delete": {"token": generate_token("jan@kowalski.xyz")}}
    response = response = await client.request(
        method="DELETE",
        url=app.url_path_for("delete_user"),
        content=json.dumps(delete),
    )
    assert response.status_code == HTTP_500_INTERNAL_SERVER_ERROR
