import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from starlette.routing import Route
from starlette.status import HTTP_200_OK

pytestmark = pytest.mark.asyncio


async def test_about_route_if_status_code_is_ok(app: FastAPI, client: AsyncClient):
    print("XDDD")
    response = await client.request("GET", app.url_path_for("index_router"))
    assert response.status_code == HTTP_200_OK
