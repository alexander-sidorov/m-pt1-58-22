from hw.mikita_karmanaw.lesson12.lesson import HttpRequest
from hw.mikita_karmanaw.lesson12.lesson import HttpResponse
from hw.mikita_karmanaw.lesson12.lesson import Url


def task_01_test() -> None:
    url1 = Url("http://google.com")
    url2 = Url("postgresql://u:p@db:5432/dbname?opt=1&xyz=2#f")
    url3 = Url("vnc://user@host?query=q")
    url4 = Url("vnc://user@host/?query=q")
    url5 = Url("ftp://a.b.c.host/p/a/t/h?query=q&f=f#f")

    assert url1.scheme == "http"
    assert url1.username is None
    assert url1.password is None
    assert url1.host == "google.com"
    assert url1.port is None
    assert url1.path is None
    assert url1.query is None
    assert url1.fragment is None

    assert url2.scheme == "postgresql"
    assert url2.username == "u"
    assert url2.password == "p"  # noqa: S105
    assert url2.host == "db"
    assert url2.port == 5432
    assert url2.path == "/dbname"
    assert url2.query == "opt=1&xyz=2"
    assert url2.fragment == "f"

    assert url3.scheme == "vnc"
    assert url3.username == "user"
    assert url3.password is None
    assert url3.host == "host"
    assert url3.port is None
    assert url3.path is None
    assert url3.query == "query=q"
    assert url3.fragment is None

    assert url4.scheme == "vnc"
    assert url4.username == "user"
    assert url4.password is None
    assert url4.host == "host"
    assert url4.port is None
    assert url4.path == "/"
    assert url4.query == "query=q"
    assert url4.fragment is None

    assert url5.scheme == "ftp"
    assert url5.username is None
    assert url5.password is None
    assert url5.host == "a.b.c.host"
    assert url5.port is None
    assert url5.path == "/p/a/t/h"
    assert url5.query == "query=q&f=f"
    assert url5.fragment == "f"


def task_02_test() -> None:
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


def task_03_test() -> None:
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
