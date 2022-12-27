import json
from contextlib import suppress
from typing import Any
from urllib.parse import urlparse


class Url:
    def __init__(self, url: Any) -> None:
        url = urlparse(url)
        self.scheme = url.scheme
        self.username = url.username
        self.password = url.password
        self.host = url.hostname
        self.port = url.port
        if url.path and len(url.path) > 0:
            self.path = url.path
        else:
            self.path = None
        if url.query and len(url.query) > 0:
            self.query = url.query
        else:
            self.query = None
        if url.fragment and len(url.fragment) > 0:
            self.fragment = url.fragment
        else:
            self.fragment = None


class HttpRequest:
    def __init__(self, request_on_server: Any) -> None:

        request = request_on_server.strip()

        title_end = request.find("\n")
        title = request[:title_end]
        title = title.split()
        self.method, self.path, self.http_version = title

        self.body: None = None

        request = (request[title_end:]).strip("\n")  # noqa E203

        heads = request.split("\n")

        self.headers: dict = {}
        for i in heads:
            i = i.split(":")
            i[0] = i[0].replace(" ", "")
            i[1] = i[1].replace(" ", "")
            self.headers.update({i[0]: i[1]})


class HttpResponse:
    def __init__(self, response_from_server: Any):

        response = response_from_server.strip()

        self.http_version: str = (response[0:8]).strip(" \n")

        status_begin = response.find(" ")
        status_end = response.find(" ", status_begin + 1)
        self.status_code: int = int(
            (response[status_begin + 1 : status_end]).strip(" \n")  # noqa E203
        )

        reason_end = response.find("\n", status_end)
        self.reason: str = (response[status_end:reason_end]).strip(" \n")

        body_start = response.find("{")
        headers = (response[reason_end:body_start]).strip("\n ")

        headers_list = headers.split("\n")
        self.headers = {}
        for i in headers_list:
            i = i.split(":")
            i[0] = i[0].replace(" ", "")
            i[1] = i[1].replace(" ", "")
            with suppress(ValueError):
                i[1] = int(i[1])
            self.headers.update({i[0]: i[1]})

        body_end = response.find("}")
        self.body = response[body_start : body_end + 1]  # noqa E203

    def is_valid(self) -> Any:
        return len(self.body) == self.headers["Content-Length"]

    def json(self) -> Any:
        if "json" in self.headers["Content-Type"]:
            body = json.loads(self.body)
            return body
        return None
