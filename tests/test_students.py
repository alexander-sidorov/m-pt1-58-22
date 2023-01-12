import httpx
import pytest

pytestmark = [
    pytest.mark.anyio,
]


async def test_success(asgi_client: httpx.AsyncClient) -> None:
    url = "api/students/"

    rs: httpx.Response = await asgi_client.get(
        url, headers={"host": "localhost"}
    )
    assert rs.status_code == 200

    payload = rs.json()
    assert isinstance(payload, dict)

    data = payload.get("data")
    assert isinstance(data, dict)
    assert len(data["students"]) == 16
    for item in data["students"]:
        assert isinstance(item, dict)
        assert item.keys() == {"name"}
