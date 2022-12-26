import hw.eugene_lubimov.lesson12.lesson12 as les


def test_pars_url() -> None:

    url = les.Url("http://google.com")
    assert url.scheme == "http"
    assert url.username is None
    assert url.password is None
    assert url.host == "google.com"
    assert url.port is None
    assert url.path is None
    assert url.query is None
    assert url.fragment is None

    url = les.Url("postgresql://u:p@db:5432/dbname?opt=1&xyz=2#f")
    assert url.scheme == "postgresql"
    assert url.username == "u"
    assert url.password == "p"  # noqa: S105
    assert url.host == "db"
    assert url.port == 5432
    assert url.path == "/dbname"
    assert url.query == "opt=1&xyz=2"
    assert url.fragment == "f"

    url = les.Url("vnc://user@host?query=q")
    assert url.scheme == "vnc"
    assert url.username == "user"
    assert url.password is None
    assert url.host == "host"
    assert url.port is None
    assert url.path is None
    assert url.query == "query=q"
    assert url.fragment is None

    url = les.Url("vnc://user@host/?query=q")
    assert url.scheme == "vnc"
    assert url.username == "user"
    assert url.password is None
    assert url.host == "host"
    assert url.port is None
    assert url.path == "/"
    assert url.query == "query=q"
    assert url.fragment is None

    url = les.Url("ftp://a.b.c.host/p/a/t/h?query=q&f=f#f")
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

    req = les.HttpRequest(message)

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

    message = """HEAD /docs/python_3/library/urllib.parse.html HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: digitology.tech
User-Agent: HTTPie/3.2.1


"""
    req1 = les.HttpRequest(message)

    assert req1.method == "HEAD"
    assert req1.path == "/docs/python_3/library/urllib.parse.html"
    assert req1.http_version == "HTTP/1.1"
    assert req1.headers["Accept"] == "*/*"
    assert req1.body is None


def test__http_response() -> None:

    message = """HTTP/1.1 404 NOT FOUND
Content-Length: 48
Content-Type: application/json
Server: gunicorn/19.9.0

{"status_code": 404, "description": "no access"}
"""

    resp = les.HttpResponse(message)

    assert resp.status_code == 404
    assert resp.reason == "Not Found"
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

    resp = les.HttpResponse(message)

    assert not resp.is_valid()
    assert resp.json() is None

    message = """HTTP/1.1 404 NOT FOUND
Content-Length: 48
Content-Type: text/html
Server: gunicorn/19.9.0

{"status_code": 404, "description": "no access"}
"""

    resp = les.HttpResponse(message)

    assert resp.is_valid()
    assert resp.json() is None

    message = """HTTP/1.1 404 NOT FOUND
Content-Length: 48
Content-Type: application/json
Server: gunicorn/19.9.0

!!!!!!!
"""

    resp = les.HttpResponse(message)

    assert resp.status_code == 404
    assert resp.reason == "Not Found"
    assert resp.http_version == "HTTP/1.1"
    assert resp.headers == {
        "Content-Length": 48,
        "Content-Type": "application/json",
        "Server": "gunicorn/19.9.0",
    }
    assert resp.body == "!!!!!!!"
    assert not resp.is_valid()
    assert resp.json() is None
