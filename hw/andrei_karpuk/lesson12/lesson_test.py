from hw.andrei_karpuk.lesson12.lesson import HttpRequest
from hw.andrei_karpuk.lesson12.lesson import HttpResponse
from hw.andrei_karpuk.lesson12.lesson import Url


def test_url() -> None:
    url = Url("http://google.com")
    assert url.scheme == "http"
    assert url.username is None
    assert url.password is None
    assert url.host == "google.com"
    assert url.port is None
    assert url.path == ""
    assert url.query == ""
    assert url.fragment == ""

    url = Url("postgresql://u:p@db:5432/dbname?opt=1&xyz=2#f")
    assert url.scheme == "postgresql"
    assert url.username == "u"
    assert url.password == "p"  # noqa: S105
    assert url.host == "db"
    assert url.port == 5432
    assert url.path == "/dbname"
    assert url.query == "opt=1&xyz=2"
    assert url.fragment == "f"

    url = Url("vnc://user@host?query=q")
    assert url.scheme == "vnc"
    assert url.username == "user"
    assert url.password is None
    assert url.host == "host"
    assert url.port is None
    assert url.path == ""
    assert url.query == "query=q"
    assert url.fragment == ""

    url = Url("vnc://user@host/?query=q")
    assert url.scheme == "vnc"
    assert url.username == "user"
    assert url.password is None
    assert url.host == "host"
    assert url.port is None
    assert url.path == "/"
    assert url.query == "query=q"
    assert url.fragment == ""

    url = Url("ftp://a.b.c.host/p/a/t/h?query=q&f=f#f")
    assert url.scheme == "ftp"
    assert url.username is None
    assert url.password is None
    assert url.host == "a.b.c.host"
    assert url.port is None
    assert url.path == "/p/a/t/h"
    assert url.query == "query=q&f=f"
    assert url.fragment == "f"


def test_http_request() -> None:
    message = """HEAD / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: github.com
User-Agent: HTTPie/3.2.1
"""
    req = HttpRequest(message)
    assert req.method == "HEAD"
    assert req.path == "/"
    assert req.http_version == "HTTP/1.1"
    assert req.headers == {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Host": "github.com",
        "User-Agent": "HTTPie/3.2.1",
    }
    assert req.body is None


def test_http_response() -> None:
    message1 = """HTTP/1.1 404 NOT FOUND
Content-Length: 48
Content-Type: application/json
Server: gunicorn/19.9.0
{"status_code": 404, "description": "no access"}"""

    resp1 = HttpResponse(message1)

    assert resp1.status_code == 404
    assert resp1.reason == "Not Found"
    assert resp1.http_version == "HTTP/1.1"
    assert resp1.headers == {
        "Content-Length": 48,
        "Content-Type": "application/json",
        "Server": "gunicorn/19.9.0",
    }
    assert resp1.body == '{"status_code": 404, "description": "no access"}'
    assert resp1.is_valid()
    assert resp1.json() == {"status_code": 404, "description": "no access"}

    message2 = """HTTP/1.1 404 NOT FOUND
Content-Length: 49
Content-Type: text/html
Server: gunicorn/19.9.0
{"status_code": 404, "description": "no access"}"""

    resp2 = HttpResponse(message2)

    assert not resp2.is_valid()
    assert resp2.json() is None

    message3 = """HTTP/1.1 404 NOT FOUND
Content-Length: 48
Content-Type: text/html
Server: gunicorn/19.9.0
{"status_code": 404, "description": "no access"}"""

    resp3 = HttpResponse(message3)

    assert resp3.is_valid()
    assert resp3.json() is None

    message4 = """HTTP/1.1 404 NOT FOUND
Content-Length: 48
Content-Type: application/json
Server: gunicorn/19.9.0
"""

    resp4 = HttpResponse(message4)

    assert resp4.body is None
    assert resp4.json() is None
