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
