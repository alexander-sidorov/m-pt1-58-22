from hw.dmitry_mihkailiuk.lesson12.lesson import Request
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


def test_02() -> None:

    st = """HEAD /docs/cli HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: httpie.io
User-Agent: HTTPie/3.2.1"""

    request = Request(st)
    assert request.method == "HEAD"
    assert request.path == "/docs/cli"
    assert request.version == "HTTP/1.1"
    assert request.headers == {
        "Accept": " */*",
        "Accept-Encoding": " gzip, deflate",
        "Connection": " keep-alive",
        "Host": " httpie.io",
        "User-Agent": " HTTPie/3.2.1",
    }
