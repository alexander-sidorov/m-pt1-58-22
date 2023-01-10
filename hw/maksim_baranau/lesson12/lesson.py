import json
from typing import Any


class Url:
    def __init__(self, url: str) -> None:  # noqa: CCR001
        self.scheme = None
        self.username = None
        self.password = None
        self.host = None
        self.port = None
        self.path = None
        self.query = None
        self.fragment = None

        self.scheme = url[: url.find("://")]
        urlpos = url.find("://") + 3
        url = url[urlpos:]
        if "#" in url:
            self.fragment = url[url.find("#") + 1:]
            url = url[: url.find("#")]
        if "@" in url:
            if ":" in url:
                self.username = url[: url.find(":")]
                url = url[url.find(":") + 1:]
                self.password = url[: url.find("@")]
                url = url[url.find("@") + 1:]
            else:
                self.username = url[: url.find("@")]
                url = url[url.find("@") + 1:]
                if "/" in url:
                    self.host = url[: url.find("/")]
                    url = url[url.find("/") + 1:]
                if "?" in url:
                    urlhost = url[: url.find("?")]
                    if not urlhost:
                        self.host = None
                    else:
                        self.host = urlhost
                        url = url[url.find("?"):]
                else:
                    self.host = url
        else:
            if "/" in url or "?" in url:
                self.host = url[: url.find("/")]
                url = url.replace(self.host, "")
            else:
                self.host = url
        if "?" in url:
            self.query = url[url.find("?") + 1:]
            url = url[: url.find("?")]
        if ":" in url:
            self.host = url[: url.find(":")]
            url = url[url.find(":") + 1:]
        if "/" in url:
            self.path = url[url.find("/"):]
            url = url[: url.find("/")]
        if url.isnumeric():
            self.port = url


class HttpRequest:
    def __init__(self, req: str) -> None:
        self.method: None | str = None
        self.path: None | str = None
        self.http_version: None | str = None
        self.headers: dict[str, str] = {}
        self.body: None | str = None
        self.body = self.body if self.body else None
        req = req[: req.find("\n\n")]
        lines = req.splitlines()
        head = lines[0].split(" ")
        self.method, self.path, self.http_version = head
        del lines[0]
        for line in lines:
            header = line.split(": ")
            self.headers[header[0]] = header[1]


class HttpResponse:
    def __init__(self, get: str):
        self.body: str | None
        line, self.body = get.split("\n\n", 1)
        line_list = line.split("\n")
        self.http_version, other = line_list[0].split(" ", 1)
        status_code, self.reason = other.split(" ", 1)
        self.status_code = int(status_code)
        line_list = line_list[1:]
        self.headers: dict[str, int | str] = {}
        for i in line_list:
            key, value = i.strip().split(":", 1)
            if key == "Content-Length":
                self.headers[key] = int(value)
            else:
                self.headers[key] = value.strip()
        self.body = self.body if self.body else None

    def is_valid(self) -> bool:
        if self.body is not None:
            return self.headers["Content-Length"] == len(self.body)
        else:
            return False

    def json(self) -> Any:
        if self.headers["Content-Type"] == "application/json":
            try:
                if self.body is not None:
                    return json.loads(self.body)
            except json.decoder.JSONDecodeError:
                return None
        else:
            return None
