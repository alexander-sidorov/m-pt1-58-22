def test_01_urlsplit(url: str) -> dict:

    comps = task_01_urlsplit("http://user:password@host:1234/resourse")
    assert comps("scheme") == "http"
    assert comps("userinfo") == "user:password"
    assert comps("host") == "host"
    assert comps("port") == "1234"