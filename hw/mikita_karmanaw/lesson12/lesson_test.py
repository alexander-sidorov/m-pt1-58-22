from hw.mikita_karmanaw.lesson12.lesson import task_01_urlsplit


def task_01_test() -> None:
    address = "vnc://user:pass@localhost:8000/s/cree/n1?q=2#x"
    assert address is str
    assert task_01_urlsplit(address) == {
        "scheme": "vnc",
        "user": "user",
        "password": "pass",
        "host": "localhost",
        "port": 8000,
        "path": "/s/cree/n1",
        "query": "q=2",
        "fragment": "x",
    }
    request = "https://user@site.by/page#frag"
    request2 = "https://site.by/page?q=a"
    assert request
    assert request2
    assert task_01_urlsplit(request) == {
        "scheme": "https",
        "user": "user",
        "host": "site.by",
        "path": "/page",
        "fragment": "frag",
    }
    assert task_01_urlsplit(request2) == {
        "scheme": "https",
        "host": "site.by",
        "path": "/page",
        "query": "q=a",
    }