from hw.dmitry_mihkailiuk.lesson12.lesson import HttpRequest
from hw.dmitry_mihkailiuk.lesson12.lesson import HttpResponse
from hw.dmitry_mihkailiuk.lesson12.lesson import Url


def test_url() -> None:
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

    url = Url("ftp://a.b.c.host/p/a/t/h#f")
    assert url.scheme == "ftp"
    assert url.username is None
    assert url.password is None
    assert url.host == "a.b.c.host"
    assert url.port is None
    assert url.path == "/p/a/t/h"
    assert url.query is None
    assert url.fragment == "f"

    url = Url("vcn://user:pass@localhost:8000/s/cree/n1?q=2#x")
    assert url.scheme == "vcn"
    assert url.username == "user"
    assert url.password == "pass"  # noqa: S105
    assert url.host == "localhost"
    assert url.port == 8000
    assert url.path == "/s/cree/n1"
    assert url.query == "q=2"
    assert url.fragment == "x"

    url = Url("http://google.com:8000")
    assert url.scheme == "http"
    assert url.username is None
    assert url.password is None
    assert url.host == "google.com"
    assert url.port == 8000
    assert url.path is None
    assert url.query is None
    assert url.fragment is None


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

    message = """HEAD /docs/cli HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: httpie.io
User-Agent: HTTPie/3.2.1

<body>
"""

    req = HttpRequest(message)

    assert req.method == "HEAD"
    assert req.path == "/docs/cli"
    assert req.http_version == "HTTP/1.1"
    assert req.headers == {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Host": "httpie.io",
        "User-Agent": "HTTPie/3.2.1",
    }

    assert req.body == "<body>\n"


def test_http_response() -> None:

    message = """HTTP/1.1 404 NOT FOUND
Content-Length: 48
Content-Type: application/json
Server: gunicorn/19.9.0

{"status_code": 404, "description": "no access"}"""

    resp = HttpResponse(message)

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

{"status_code": 404, "description": "no access"}"""

    resp = HttpResponse(message)

    assert not resp.is_valid()
    assert resp.json() is None

    message = """HTTP/1.1 404 NOT FOUND
Content-Length: 48
Content-Type: text/html
Server: gunicorn/19.9.0

{"status_code": 404, "description": "no access"}"""

    resp = HttpResponse(message)

    assert resp.is_valid()
    assert resp.json() is None

    message = """HTTP/1.1 404 NOT FOUND
Content-Length: 48
Content-Type: application/json
Server: gunicorn/19.9.0

'status_code': 404, 'description': 'no access'"""

    resp = HttpResponse(message)

    assert resp.body == "'status_code': 404, 'description': 'no access'"
    assert not resp.is_valid()
    assert resp.json() is None

    message = """HTTP/1.1 404 NOT FOUND
Content-Length: 48
Content-Type: application/json
Server: gunicorn/19.9.0

"""

    resp = HttpResponse(message)

    assert resp.body is None
    assert not resp.is_valid()
    assert resp.json() is None
