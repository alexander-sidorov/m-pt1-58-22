import json
from contextlib import suppress
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
        url = url[url.find("://") + 3:]
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
                    if urlhost == "":
                        ...
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
