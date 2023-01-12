from urllib.parse import urlencode

import httpx
import pytest

pytestmark = [
    pytest.mark.anyio,
]


@pytest.mark.parametrize(
    "url",
    [
        "/~/alexander_sidorov/api/04/01/",
    ],
)
@pytest.mark.parametrize(
    "rubles,coins,amount,expected",
    [
        (0, 0, 0, 0),
        (0, 1, -3, -0.03),
        (0, 1, 3, 0.03),
        (-1, -1, 0, 0),
        (-1, -2, -3, 3.06),
        (-1, -2, 3, -3.06),
        (-1, 1, 0, 0),
        (-1, 2, -3, 2.94),
        (1, 0, -3, -3),
        (1, 0, 3, 3),
        (1, -1, 0, 0),
        (1, -2, -3, -2.94),
        (1, 1, 0, 0),
        (1, 2, -3, -3.06),
        (1, 2, 3, 3.06),
    ],
)
async def test_success(
    asgi_client: httpx.AsyncClient,
    url: str,
    rubles: int,
    coins: int,
    amount: int,
    expected: float,
) -> None:
    query = urlencode({"r": rubles, "c": coins, "a": amount})
    url = f"{url}?{query}"

    rs: httpx.Response = await asgi_client.get(
        url, headers={"host": "localhost"}
    )
    assert rs.status_code == 200

    payload = rs.json()
    assert isinstance(payload, dict)

    data = payload.get("data")
    assert isinstance(data, float)
    assert abs(data - expected) < 0.01
