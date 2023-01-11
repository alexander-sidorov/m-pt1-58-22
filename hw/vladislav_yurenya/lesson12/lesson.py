import json
from typing import Any
from urllib.parse import urlparse


class Url:
    def __init__(self, url: str):
        self.url = url
        new = urlparse(self.url)
        self.scheme = new.scheme or None
        self.username = new.username or None
        self.password = new.password or None
        self.host = new.hostname or None
        self.port = new.port or None
        self.path = new.path or None
        self.query = new.query or None
        self.fragment = new.fragment or None


class HttpRequest:
    def __init__(self, req: str):
        self.req: str | Any
        self.body: None | str = None
        body = req.find("\n\n") + 2
        self.body = req[body:]
        if self.body == "":
            self.body = None
        self.req = req.split("\n")
        new = self.req[0].split(" ")
        self.method = new[0]
        self.path = new[1]
        self.http_version = new[2]
        qef = self.req[1:-2]
        self.headers: dict[str, Any] = {}
        for i in qef:
            count = i.split(": ")
            self.headers[count[0]] = count[1]


class HttpResponse:
    def __init__(self, url: str):
        self.url = url
        new = self.url.split()
        self.http_version = new[0]
        self.status_code = int(new[1])
        new_0 = " ".join(new[2:4])
        self.reason = new_0.title()
        for_headers = self.url.split("\n")
        for_headers = [for_headers.strip(" ") for for_headers in for_headers]
        for_headers[2].replace("\n", "")
        for_headers = for_headers[1:4]
        for_headers[2] = for_headers[2].replace("\n", "")
        self.headers: dict[str, Any] = {}
        for header in for_headers:
            count = header.split(": ")
            self.headers[count[0]] = count[1]
        for key in self.headers.keys():
            if key == "Content-Length":
                self.headers[key] = int(self.headers["Content-Length"])
        self.body: str | bytes
        new_body = list(url.split("\n\n"))
        new_bod = new_body[1].strip()
        self.body = new_bod

    def is_valid(self) -> bool:
        if self.body is not None and self.headers["Content-Length"] == len(
            self.body
        ):
            return True

    def json(self) -> Any:
        if self.headers["Content-Type"] == "application/json":
            return json.loads(self.body)
        else:
            return None
