from fastapi.applications import FastAPI
import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from starlette.status import HTTP_404_NOT_FOUND

pytestmark = pytest.mark.asyncio


async def test_http_errors(client: AsyncClient):
    response = await client.request("GET", "http://test.com/blah/blah")
    assert response.status_code == HTTP_404_NOT_FOUND
