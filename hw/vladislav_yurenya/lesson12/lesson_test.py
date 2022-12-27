import pytest

from hw.vladislav_yurenya.lesson12.lesson import HttpRequest
from hw.vladislav_yurenya.lesson12.lesson import Url


def test_01_urlsplit() -> None:
    url = Url("http://google.com")
    assert url.scheme == "http"
    assert url.username is None
    assert url.password is None
    assert url.host == "google.com"
    assert url.port is None
    assert url.path is None
    assert url.query is None
    assert url.fragment is None

    url = Url("postgresql://u:p@db:5432/dbname?opt=1&xyz=2#f")
    assert url.scheme == "postgresql"
    assert url.username == "u"
    assert url.password == "p"
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
    assert url.path is None
    assert url.query == "query=q"
    assert url.fragment is None

    url = Url("vnc://user@host/?query=q")
    assert url.scheme == "vnc"
    assert url.username == "user"
    assert url.password is None
    assert url.host == "host"
    assert url.port is None
    assert url.path == "/"
    assert url.query == "query=q"
    assert url.fragment is None

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
    message_2 = """HEAD / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: github.com
User-Agent: HTTPie/3.2.1

Hard"""

    req = HttpRequest(message_2)

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
    assert req.body == "Hard"
