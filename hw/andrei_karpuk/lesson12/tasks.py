from urllib.parse import urlparse


def task_01_urlsplit(url: str) -> dict:
    url_cort = urlparse(url)
    return {
        "scheme": url_cort.scheme,
        "user": url_cort.username,
        "password": url_cort.password,
        "host": url_cort.hostname,
        "port": url_cort.port,
        "path": url_cort.path,
        "query": url_cort.query,
        "fragment": url_cort.fragment,
    }


class Request:
    __init__git

GET /alexander-sidorov/m-pt1-58-22 HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: github.com
User-Agent: HTTPie/3.2.1
