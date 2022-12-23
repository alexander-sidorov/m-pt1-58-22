from urllib.parse import urlparse


def task_01_urlsplit(url: str) -> dict:
    dicturl = urlparse(url)
    return {
        "shema": dicturl.scheme,
        "user": dicturl.username,
        "password": dicturl.password,
        "host": dicturl.hostname,
        "port": dicturl.port,
        "path": dicturl.path,
        "query": dicturl.query,
        "fragment": dicturl.fragment,
    }
