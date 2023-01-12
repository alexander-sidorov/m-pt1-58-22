import httpx


async def test_success(asgi_client: httpx.AsyncClient) -> None:
    url = "students/"

    rs: httpx.Response = await asgi_client.get(
        url, headers={"host": "localhost"}
    )
    assert rs.status_code == 200

    payload = rs.json()
    assert isinstance(payload, dict)

    data = payload.get("data")
    assert isinstance(data, list)
    assert len(data) == 16
    for item in data:
        assert isinstance(item, dict)
        assert item.keys() == {"name"}
