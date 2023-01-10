from hw.igor_maksimov.lesson12.tasks import task_01_urlsplit

url = "vnc://user:pass@localhost:8000/s/cree/n1?q=2#x"


def test_task_01_urlsplit() -> None:
    assert task_01_urlsplit(url) == {
        "scheme": "vnc",
        "user": "user",
        "password": "pass",
        "host": "localhost",
        "port": 8000,
        "path": "/s/cree/n1",
        "query": "q=2",
        "fragment": "x",
    }
