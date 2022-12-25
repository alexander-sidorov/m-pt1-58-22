import json
from typing import Any


class Url:
    def __init__(self, url: str):
        self.scheme = None
        self.username = None
        self.password = None
        self.host = None
        self.port = None
        self.path = None
        self.query = None
        self.fragment = None

        self.scheme, other = url.split("://")

        if "@" in other:
            us_ps, other = other.split("@")
            if ":" in us_ps:
                self.username, self.password = us_ps.split(":")
            else:
                self.username = us_ps

        if "#" in other:
            other, self.fragment = other.rsplit("#")
            if "?" in other:
                other, self.query = other.rsplit("?")
        elif "?" in other:
            other, self.query = other.rsplit("?")

        if "/" in other:
            ho_po, path = other.split("/", 1)
            self.path = "/" + path
            if ":" in ho_po:
                self.host, port = ho_po.split(":")
                self.port = int(port)
            else:
                self.host = ho_po
        elif ":" in other:
            self.host, port = other.split(":")
            self.port = int(port)
        else:
            self.host = other


class HttpRequest:
    def __init__(self, get: str):
        line, self.body = get.split("\n\n", 1)
        self.body = self.body.strip()
        line_list = line.split("\n")
        self.method, self.path, self.http_version = line_list[0].split(" ")
        line_list = line_list[1:]
        self.headers = {}
        for i in line_list:
            key, value = i.strip().split(":", 1)
            self.headers[key] = value.strip()
        if not self.body:
            self.body = None


class HttpResponse:
    def __init__(self, get: str):
        line, self.body = get.split("\n\n", 1)
        self.body = self.body.strip()
        line_list = line.split("\n")
        self.http_version, other = line_list[0].split(" ", 1)
        status_code, self.reason = other.split(" ", 1)
        self.status_code = int(status_code)
        line_list = line_list[1:]
        self.headers = {}
        for i in line_list:
            key, value = i.strip().split(":", 1)
            if key == "Content-Length":
                self.headers[key] = int(value)
            else:
                self.headers[key] = value.strip()

    def is_valid(self) -> bool:
        return self.headers["Content-Length"] == len(self.body)

    def json(self) -> Any:
        if self.headers["Content-Type"] == "application/json":
            try:
                return json.loads(self.body)
            except json.decoder.JSONDecodeError:
                return None
        else:
            return None
