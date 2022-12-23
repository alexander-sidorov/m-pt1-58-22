import hw.vadim_zharski.lesson12.lesson as l_12


def test_01() -> None:
    test_url = l_12.UrlParser("http://user:password@host:1234/resourse")
    next_url = l_12.UrlParser("vnc://user:pass@localhost:8000/s/cree/n1?q=2#x")
    assert next_url.splitter() == {
        "scheme": "vnc",
        "user": "user",
        "password": "pass",
        "host": "localhost",
        "port": "8000",
        "path": "/s/cree/n1",
        "query": "q=2",
        "fragment": "x"
    }