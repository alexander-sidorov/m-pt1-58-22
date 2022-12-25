from urllib.parse import urlparse

import pytest


class Url:
    def __init__(self, url: str) -> dict:
        self.url = url
        new = urlparse(self.url)
        self.url = new
        print(new)
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
