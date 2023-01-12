from urllib.parse import urlencode

import httpx
import pytest

pytestmark = [
    pytest.mark.anyio,
]

inf = float("inf")
nan = float("nan")


@pytest.mark.parametrize(
    "url",
    [
        "/~/alexander_sidorov/api/04/02/",
    ],
)
@pytest.mark.parametrize(
    "number,expected",
    [
        (0, 0),
        (-0.00001, -1),
        (-123.45, -1),
        (-inf, -1),
        (-nan, 1),
        (0.0, 0),
        (0.00001, 1),
        (123.45, 1),
        (inf, 1),
        (nan, 1),
    ],
)
async def test_success(
    asgi_client: httpx.AsyncClient,
    url: str,
    number: float,
    expected: int,
) -> None:
    query = urlencode({"n": number})
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
