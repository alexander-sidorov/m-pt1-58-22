from hw.maksim_lamaka.lesson12.task_01_urlsplit import task_01_urlsplit

url = "vnc://user:pass@localhost:8000/s/cree/n1?q=2#x"


def test_01_urlsplit() -> None:
    assert task_01_urlsplit(url) == {
        "shema": "vnc",
        "user": "user",
        "password": "pass",
        "host": "localhost",
        "port": 8000,
        "path": "/s/cree/n1",
        "query": "q=2",
        "fragment": "x",
    }
