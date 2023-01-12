from urllib.parse import urlencode

import httpx
import pytest

pytestmark = [
    pytest.mark.anyio,
]


@pytest.mark.parametrize(
    "url",
    [
        "/~/alexander_sidorov/api/04/03/",
    ],
)
@pytest.mark.parametrize(
    "s1,s2,s3,expected",
    [
        (0, 0, 0, False),
        (1, 2, 3, False),
        (2, 3, 4, True),
        (3, 4, 5, True),
    ],
)
async def test_success(
    asgi_client: httpx.AsyncClient,
    url: str,
    s1: int,
    s2: int,
    s3: int,
    expected: bool,
) -> None:
    query = urlencode({"a": s1, "b": s2, "c": s3})
    url = f"{url}?{query}"

    rs: httpx.Response = await asgi_client.get(
        url, headers={"host": "localhost"}
    )
    assert rs.status_code == 200

    payload = rs.json()
    assert isinstance(payload, dict)

    data = payload.get("data")
    assert isinstance(data, bool)
    assert data == expected
