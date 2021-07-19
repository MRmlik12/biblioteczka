import pytest
from fastapi import FastAPI
from catana.main import get_app
from asgi_lifespan import LifespanManager
from httpx import AsyncClient
from pytest_postgresql import factories


# postgresql_proc = factories.postgresql_proc(
#     port=5432, user="test", password="123", dbname="catana_db", host="localhost"
# )
# postgresql2 = factories.postgresql("postgresql_proc")


@pytest.fixture
def app() -> FastAPI:
    return get_app()


@pytest.fixture
async def initialized_app(app: FastAPI) -> FastAPI:
    async with LifespanManager(app):
        yield app


@pytest.fixture
async def client(initialized_app: FastAPI) -> AsyncClient:
    async with AsyncClient(
        app=initialized_app,
        base_url="http://test",
        headers={"Content-Type": "application/json"},
    ) as client:
        yield client
