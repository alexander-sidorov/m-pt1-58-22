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
        self.headers = " ".join(qef)
        rew = self.headers.split(" ")
        self.headers: dict[str, list] = {}
        self.headers["Accept"] = rew[1]
        self.headers["Accept-Encoding"] = " ".join(rew[3:5])
        self.headers["Connection"] = rew[6]
        self.headers["Host"] = rew[8]
        self.headers["User-Agent"] = rew[10]
