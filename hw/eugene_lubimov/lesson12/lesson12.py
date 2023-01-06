import json
from typing import Any
from typing import Optional


class Url:
    def __init__(self, url: str) -> None:

        self.username: str | None = None
        self.password: str | None = None
        self.fragment: str | None = None
        self.query: str | None = None
        self.path: str | None = None
        self.port: int | None = None
        self.scheme, other = url.split("://")
        if "@" in other:
            self.userinfo, other = other.split("@")
            if ":" in self.userinfo:
                self.username, self.password = self.userinfo.split(":")
            else:
                self.username = self.userinfo
        if "#" in other:
            other, self.fragment = other.split("#")
        if "?" in other:
            other, self.query = other.split("?")
        if "/" in other:
            ind = other.index("/")
            self.path, other = other[ind:], other[:ind]
        self.host: str = other
        if ":" in self.host:
            self.host, port = other.split(":")
            self.port = int(port)


class HttpRequest:
    def __init__(self, req: str) -> None:
        ind = req.index("\n\n") + 2
        body = req[ind:]
        self.__body = body if body else None
        self.req = req[: req.index("\n\n")].split("\n")
        first = self.req[0].split()
        self.__method, self.__path, self.__http_version = first
        self.__headers_dict: dict = {}
        for head in self.req[1:]:
            header, value = head.split(": ")
            self.__headers_dict[header] = value

    @property
    def method(self) -> str:
        return self.__method

    @property
    def path(self) -> str:
        return self.__path

    @property
    def http_version(self) -> str:
        return self.__http_version

    @property
    def headers(self) -> dict:
        return self.__headers_dict

    @property
    def body(self) -> Optional[str]:
        return self.__body


class HttpResponse:
    def __init__(self, res: str) -> None:
        ind = res.index("\n\n") + 2
        body = res[ind:]
        self.__body = body
        self.res = res[: res.index("\n\n")].split("\n")
        first = self.res[0].split()
        self.__http_version, status_code, *reason = first
        self.__status_code: int = int(status_code)
        self.__reason: str = " ".join(reason).title()
        self.__headers: dict = {}
        for head in self.res[1:]:
            header, val = head.split(": ")
            value: str | int = int(val) if val.isdigit() else val
            self.__headers[header] = value

    @property
    def http_version(self) -> str:
        return self.__http_version

    @property
    def status_code(self) -> int:
        return self.__status_code

    @property
    def reason(self) -> str:
        return self.__reason

    @property
    def headers(self) -> dict:
        return self.__headers

    @property
    def body(self) -> str:
        return self.__body

    def is_valid(self) -> Any:
        return self.__headers["Content-Length"] == len(self.body)

    def json(self) -> Any:
        if self.__headers["Content-Type"] != "application/json":
            return
        try:
            self.__json = json.loads(self.body)
        except Exception:
            return
        return self.__json
