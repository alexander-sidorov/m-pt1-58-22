from urllib.parse import urlparse


def task_01_urlsplit(url: str) -> dict:
    url_var = urlparse(url)
    return {
        "scheme": url_var.scheme,
        "user": url_var.username,
        "password": url_var.password,
        "host": url_var.hostname,
        "port": url_var.port,
        "path": url_var.path,
        "query": url_var.query,
        "fragment": url_var.fragment,
    }