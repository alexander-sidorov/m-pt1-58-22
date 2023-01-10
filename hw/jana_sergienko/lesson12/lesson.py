import json
from typing import Any
from typing import cast
from urllib.parse import urlparse


class Url:
    def __init__(self, url: str):
        new_url = urlparse(url)
        self.scheme = new_url.scheme
        self.username = new_url.username
        self.password = new_url.password
        self.host = new_url.hostname
        self.port = new_url.port
        self.path = new_url.path
        self.query = new_url.query
        self.fragment = new_url.fragment


class HttpRequest:
    def __init__(self, request: Any) -> None:

        new_request = request.strip()

        line_end = new_request.find("\n")
        line = new_request[:line_end]
        line = line.split()
        self.method, self.path, self.http_version = line

        self.body = None

        new_request = (new_request[line_end:]).strip("\n")  # noqa E203

        heads = new_request.split("\n")

        self.headers = {}
        for i in heads:
            i = i.split(": ")
            self.headers[i[0]] = i[1]


class HttpResponse:
    def __init__(self, resp: str) -> None:
        self.status_code: None | int = None
        self.reason: None | str = None
        self.http_version: None | str = None
        self.headers: dict[str, str | int] = {}
        self.body: None | str = None
        body_cut_pos = resp.find("\n\n") + 2
        self.body = resp[body_cut_pos:]
        if self.body == "":
            self.body = None
        resp = resp[: resp.find("\n\n")]
        lines = resp.splitlines()
        head = lines[0]
        self.http_version = head.partition(" ")[0]
        head_cut_pos = len(self.http_version) + 1
        head = head[head_cut_pos:]
        code = head.partition(" ")[0]
        self.status_code = int(code)
        reason_cut_pos = len(code) + 1
        self.reason = head[reason_cut_pos:].title()
        del lines[0]
        for line in lines:
            value: int | str
            header, value = line.split(": ")
            if value.isdigit():
                value = int(value)
            self.headers[header] = value

    def is_valid(self) -> bool:
        return self.body is not None and len(self.body) == self.headers.get(
            "Content-Length", 0
        )

    def json(self) -> Any:
        if self.body is None:
            return None
        content_type = cast(str, self.headers.get("Content-Type", ""))
        if "application/json" in content_type:
            return json.loads(self.body)
        return None
