import json
import re
from typing import Any
from urllib.parse import urlparse


class Url:
    def __init__(self, url: str):
        self.url = url
        new = urlparse(self.url)
        self.c = {
            "schema": new.scheme,
            "username": new.username,
            "password": new.password,
            "host": new.hostname,
            "port": new.port,
            "path": new.path,
            "query": new.query,
            "fragment": new.fragment,
        }
        self.scheme = self.c["schema"]
        self.username = self.c["username"]
        self.password = self.c["password"]
        self.host = self.c["host"]
        self.port = self.c["port"]
        self.path = self.c["path"]
        if self.path == "":
            self.path = None
        self.query = self.c["query"]
        if self.query == "":
            self.query = None
        self.fragment = self.c["fragment"]
        if self.fragment == "":
            self.fragment = None


class HttpRequest:
    def __init__(self, req: str):
        self.req: str | Any
        self.body: None | str = None
        body = req.find("\n\n") + 2
        self.body = req[body:]
        if self.body == "":
            self.body = None
        self.req = re.split("\n", req)
        new = self.req[0].split(" ")
        self.method = new[0]
        self.path = new[1]
        self.http_version = new[2]
        qef = self.req[1:]
        self.headers: dict[str, Any] = {}
        for i in range(len(qef) - 2):
            count = qef[i].split(": ")
            self.headers[count[0]] = count[1]


class HttpResponse:
    def __init__(self, url: str):
        self.url = url
        new = self.url.split()
        self.http_version = new[0]
        self.status_code = int(new[1])
        new_0 = " ".join(new[2:4])
        self.reason = new_0.title()
        new = new[4:]
        for_headers = self.url.split("\n    ")
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
        print(self.headers.values())
        left = self.url.find("{")
        self.body = self.url[left:]
        deleted = self.body.find("\n   ")
        self.body = self.body[:deleted]

    def is_valid(self) -> bool:
        return self.headers["Content-Length"] == len(self.body)

    def json(self) -> Any:
        if self.headers["Content-Type"] == "application/json":
            return json.loads(self.body)
        else:
            return None


message = """HTTP/1.1 404 NOT FOUND
    Content-Length: 48
    Content-Type: application/json
    Server: gunicorn/19.9.0

    {"status_code": 404, "description": "no access"}
    """

resp = HttpResponse(message)
