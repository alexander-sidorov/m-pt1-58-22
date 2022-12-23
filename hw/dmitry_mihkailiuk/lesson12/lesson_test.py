from hw.dmitry_mihkailiuk.lesson12.lesson import task_01_urlsplit

url = "vcn://user:pass@localhost:8000/s/cree/n1?q=2#x"


def test_01_urlsplit() -> None:
    assert task_01_urlsplit(url) == {
        "schema": "vcn",
        "user": "user",
        "password": "pass",
        "host": "localhost",
        "port": 8000,
        "query": "q=2",
        "fragment": "x",
    }
