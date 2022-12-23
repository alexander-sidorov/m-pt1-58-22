from hw.mikita_karmanaw.lesson12.lesson import task_01_urlsplit


def task_01_test() -> None:
    address = "vnc://user:pass@localhost:8000/s/cree/n1?q=2#x"
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
