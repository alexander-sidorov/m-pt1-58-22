import json
import re
from contextlib import suppress
from typing import Any


class Url:
    def __init__(self, url_site: Any) -> None:  # noqa CCR001

        self.scheme: str | None
        self.username: str | None
        self.password: str | None
        self.host: Any
        self.port: Any
        self.path: Any
        self.query: Any
        self.fragment: Any

        url = url_site.split("://")
        self.scheme = url[0]

        url = url[1]

        _user = re.search(r"\S+@", url)
        if _user is not None:
            user = _user[0][:-1]
            user_split = user.split(":")
            self.username = user_split[0]
            try:
                self.password = user_split[1]
            except IndexError:
                self.password = None
        else:
            self.username = None
            self.password = None

        if self.username is None:
            self.host = re.search(r"://[0-9a-zA-Z.]+", url_site)
            assert self.host is not None
            self.host = self.host[0][3:]
        else:
            self.host = re.search(r"@[0-9a-zA-Z.]+", url_site)
            assert self.host is not None
            self.host = self.host[0][1:]

        self.port = re.search(r"(:\d{1,4})", url)
        if self.port is not None:
            self.port = int(self.port[0][1:])

        self.path = re.search(r"/[0-9a-zA-Z/]*", url)
        if self.path is not None:
            self.path = self.path[0]

        self.query = re.search(r"\?[^#]+", url)
        if self.query is not None:
            self.query = self.query[0][1:]

        self.fragment = re.search(r"#[a-z]", url)
        if self.fragment is not None:
            self.fragment = self.fragment[0][1:]


class HttpRequest:
    def __init__(self, request_on_server: Any) -> None:

        request = request_on_server.strip()

        title_end = request.find("\n")
        title = request[:title_end]
        title = title.split()
        self.method, self.path, self.http_version = title

        self.body = None

        request = (request[title_end:]).strip("\n")  # noqa E203

        heads = request.split("\n")

        self.headers = {}
        for i in heads:
            i = i.split(": ")
            self.headers[i[0]] = i[1]


class HttpResponse:
    def __init__(self, response_from_server: Any):

        response = response_from_server.strip()

        title_end = response.find("\n")
        title = response[:title_end]
        title = title.split(" ", 2)
        title[1] = int(title[1])
        self.http_version, self.status_code, self.reason = title

        if "\n\n" in response:
            body_start = response.find("\n\n")
            self.body = response[body_start + 2 :]  # noqa E203
        else:
            body_start = None
            self.body = None

        headers_list = (response[title_end:body_start]).strip("\n ")
        headers_list = headers_list.split("\n")
        self.headers = {}
        for i in headers_list:
            i = i.split(": ")
            with suppress(ValueError):
                i[1] = int(i[1])
            self.headers[i[0]] = i[1]

    def is_valid(self) -> Any:
        return len(self.body) == self.headers["Content-Length"]

    def json(self) -> Any:
        if "json" in self.headers["Content-Type"]:
            body = json.loads(self.body)
            return body
        return None
