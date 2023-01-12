from urllib.parse import urlencode

import httpx
import pytest

pytestmark = [
    pytest.mark.anyio,
]


@pytest.mark.parametrize(
    "url",
    [
        "/~/alexander_sidorov/api/04/04/",
    ],
)
@pytest.mark.parametrize(
    "text,expected",
    [
        ("", True),
        ("abba", True),
        ("abc", False),
        ("abcba", True),
    ],
)
async def test_success(
    asgi_client: httpx.AsyncClient,
    url: str,
    text: str,
    expected: int,
) -> None:
    query = urlencode({"t": text})
    url = f"{url}?{query}"

    rs: httpx.Response = await asgi_client.get(
        url, headers={"host": "localhost"}
    )
    assert rs.status_code == 200

    payload = rs.json()
    assert isinstance(payload, dict)

    data = payload.get("data")
    assert isinstance(data, int)
    assert data == expected
