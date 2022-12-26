import json
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
    def __init__(self, request: str) -> None:

        request = request.strip()

        self.body: None = None

        methed_end = request.find(" ")
        self.method: str = (request[0:methed_end]).strip()

        path_begin = request.find(" ")
        path_end = request.find(" ", path_begin + 1)
        self.path: str = (
            request[path_begin + 1 : path_end]  # noqa E203
        ).strip()

        http_begin = request.find("HTTP")
        self.http_version: str = (
            request[http_begin : (http_begin + 9)]  # noqa E203
        ).strip("\n")

        request = (request[http_begin + 8 :]).strip("\n")  # noqa E203

        heads = request.split("\n")

        self.headers: dict = {}
        for _ in heads:
            _ = _.split(":")
            _[0] = _[0].replace(" ", "")
            _[1] = _[1].replace(" ", "")
            self.headers.update({_[0]: _[1]})


class HttpResponse:
    def __init__(self, response: str):

        response = response.strip()

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
        for _ in headers_list:
            _ = _.split(":")
            _[0] = _[0].replace(" ", "")
            _[1] = _[1].replace(" ", "")
            try:  # noqa SIM105
                _[1] = int(_[1])
            except ValueError:
                pass
            self.headers.update({_[0]: _[1]})

        body_end = response.find("}")
        self.body = response[body_start : body_end + 1]  # noqa E203

    def is_valid(self) -> Any:
        return len(self.body) == self.headers["Content-Length"]

    def json(self) -> Any:
        if "json" in self.headers["Content-Type"]:
            body = json.loads(self.body)
            return body
        return None
