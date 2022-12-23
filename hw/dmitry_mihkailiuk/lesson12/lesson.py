from urllib.parse import urlparse


def task_01_urlsplit(url: str) -> dict:
    url_c = urlparse(url)
    return {
        "schema": url_c.scheme,
        "user": url_c.username,
        "password": url_c.password,
        "host": url_c.hostname,
        "port": url_c.port,
        "query": url_c.query,
        "fragment": url_c.fragment,
    }


class Request:
    def __init__(self, get: str):
        line = get.split("\n")
        self.method, self.path, self.version = line[0].split(" ")
        line = line[1::]
        self.headers = {}
        for i in line:
            key, value = i.split(":")
            self.headers[key] = value
