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
        new = new[4:]
        self.headers = {
            "Content-Length": int(new[1]),
            "Content-Type": new[3],
            "Server": new[5],
        }
        left = self.url.find("{")
        self.body = self.url[left:]
        deleted = self.body.find("\n   ")
        self.body = self.body[:deleted]

    def is_valid(self) -> bool:
        if self.headers["Content-Length"] == len(self.body):
            return True

    def json(self) -> Any:
        try:
            if "application/json" in self.headers["Content-Type"]:
                return json.loads(self.body)
            raise JSONDecodeError
        except:
            return None
