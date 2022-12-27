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
    def __init__(self, url: str):
        self.url: str | Any
        self.body: None | str = None
        body = url.find("\n\n") + 2
        self.body = url[body:]
        if self.body == "":
            self.body = None
        self.url = url
        self.url = re.split('" "|\n', self.url)
        new = self.url[0].split(" ")
        self.method = new[0]
        self.path = new[1]
        self.http_version = new[2]
        qef = self.url[1:]
        headers = " ".join(qef)
        rew = headers.split(" ")
        self.headers: dict[str, Any] = {}
        self.headers["Accept"] = rew[1]
        self.headers["Accept-Encoding"] = " ".join(rew[3:5])
        self.headers["Connection"] = rew[6]
        self.headers["Host"] = rew[8]
        self.headers["User-Agent"] = rew[10]


class HttpResponse:
    def __init__(self, url: str):
        self.url = url
        new = self.url.split()
        self.http_version = new[0]
        self.status_code = int(new[1])
        new_0 = " ".join(new[2:4])
        self.reason = new_0.title()
        # ----------------------------ТУТ ВСЕ ГУД--------------------------#
        new = new[4:]
        print(new)
        self.headers = {
            "Content-Length": int(new[1]),
            "Content-Type": new[3],
            "Server": new[5],
        }
        # ----------------------------ТУТ ВСЕ ГУД--------------------------#
        left = self.url.find("{")
        self.body = self.url[left:]
        deleted = self.body.find("\n   ")
        self.body = self.body[:deleted]

        # ----------------------------ТУТ ВСЕ ГУД--------------------------#

    def is_valid(self):
        if self.headers["Content-Length"] == len(self.body):
            return True

        # ----------------------------ТУТ ВСЕ ГУД--------------------------#

    def json(self):
        if self.headers["Content-Type"] == "application/json":
            return json.loads(self.body)
        elif self.headers["Content-Type"] != "application/json":
            return None


message = """HTTP/1.1 404 NOT FOUND
    Content-Length: 48
    Content-Type: application/json
    Server: gunicorn/19.9.0

    {"status_code": 404, "description": "no access"}
    """

resp = HttpResponse(message)
print(resp.is_valid())
#     for i in line_list:
#         key, value = i.strip().split(":", 1)
#         if key == "Content-Length":
#             self.headers[key] = int(value)
#         else:
#             self.headers[key] = value.strip()
#     self.body = self.body if self.body else None
#
# def is_valid(self) -> bool:
#     if self.body is not None:
#         return self.headers["Content-Length"] == len(self.body)
#     else:
#         return False
#
# def json(self) -> Any:
#     if self.headers["Content-Type"] == "application/json":
#         try:
#             if self.body is not None:
#                 return json.loads(self.body)
#         except json.decoder.JSONDecodeError:
#             return None
#     else:
#         return None
