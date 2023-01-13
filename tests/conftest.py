from typing import AsyncGenerator

import httpx
import pytest

from project.asgi import application

TIMEOUT = 20


@pytest.fixture(scope="session")
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture(scope="function")
async def asgi_client() -> AsyncGenerator[httpx.AsyncClient, None]:
    async with httpx.AsyncClient(
        app=application,
        base_url="http://asgi",
        timeout=TIMEOUT,
    ) as client:
        yield client
