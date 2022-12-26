from hw.eugene_vavilov.lesson12.lesson import HttpRequest
from hw.eugene_vavilov.lesson12.lesson import HttpResponse
from hw.eugene_vavilov.lesson12.lesson import Url


def test_task_1() -> None:
    url = Url("http://google.com")
    assert url.scheme == "http"
    assert url.username is None
    assert url.password is None
    assert url.host == "google.com"
    assert url.port is None
    assert url.path is None  # в этом случае можно "" или "/"
    assert url.query is None
    assert url.fragment is None

    url = Url("postgresql://u:p@db:5432/dbname?opt=1&xyz=2#f")
    assert url.scheme == "postgresql"
    assert url.username == "u"
    assert url.password == "p"  # noqa S105
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


def test_task_2() -> None:
    req = HttpRequest(
        """HEAD / HTTP/1.1
    Accept: */*
    Accept-Encoding: gzip, deflate
    Connection: keep-alive
    Host: github.com
    User-Agent: HTTPie/3.2.1
    """
    )
    assert req.method == "HEAD"
    assert req.path == "/"
    assert req.http_version == "HTTP/1.1"
    assert req.headers == {
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate",
        "Connection": "keep-alive",
        "Host": "github.com",
        "User-Agent": "HTTPie/3.2.1",
    }
    assert req.body is None


def test_task_3() -> None:
    resp = HttpResponse(
        """HTTP/1.1 404 NOT FOUND
    Content-Length: 48
    Content-Type: application/json
    Server: gunicorn/19.9.0
    {"status_code": 404, "description": "no access"}
    """
    )

    assert resp.status_code == 404
    assert resp.reason == "NOT FOUND"
    assert resp.http_version == "HTTP/1.1"
    assert resp.headers == {
        "Content-Length": 48,
        "Content-Type": "application/json",
        "Server": "gunicorn/19.9.0",
    }
    assert resp.body == '{"status_code": 404, "description": "no access"}'
    assert resp.is_valid()
    assert resp.json() == {"status_code": 404, "description": "no access"}

    message = """HTTP/1.1 404 NOT FOUND
    Content-Length: 49
    Content-Type: text/html
    Server: gunicorn/19.9.0
    {"status_code": 404, "description": "no access"}
    """

    resp = HttpResponse(message)

    assert not resp.is_valid()
    assert resp.json() is None

    message = """HTTP/1.1 404 NOT FOUND
    Content-Length: 48
    Content-Type: text/html
    Server: gunicorn/19.9.0
    {"status_code": 404, "description": "no access"}
    """

    resp = HttpResponse(message)

    assert resp.is_valid()
    assert resp.json() is None
