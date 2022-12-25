import json


class Url:
    def __init__(self, url: str) -> None:  # noqa: CCR001
        self.scheme, other = url.split("://")
        if "@" in other:
            userinfo, other = other.split("@")
            if ":" in userinfo:
                self.username, self.password = userinfo.split(":")
            else:
                self.username, self.password = userinfo, None
        else:
            self.username, self.password = None, None
        if "#" in other:
            other, self.fragment = other.split("#")
        else:
            self.fragment = None
        if "?" in other:
            other, self.query = other.split("?")

        else:
            self.query = None
        if "/" in other:
            ind = other.index("/")
            self.path, other = other[ind:], other[:ind]
        else:
            self.path = None
        if ":" in other:
            self.host, port = other.split(":")
            self.port = int(port)
        else:
            self.host, self.port = other, None


class HttpRequest:
    def __init__(self, req: str) -> None:
        self.req = req.split("\n")
        first = self.req[0].split()
        self.__method = first[0]
        self.__path = first[1]
        self.__http_version = " ".join(first[2:])
        self.__headers_dict: dict = {}
        end = self.req.index("")
        for head in self.req[1:end]:
            header, value = head.split(": ")
            if value.isdigit():
                value = int(value)
            self.__headers_dict[header] = value
        self.__body = self.req[-2] if self.req[-2] else None

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
    def body(self) -> str | None:
        return self.__body


class HttpResponse(HttpRequest):
    def __init__(self, req: str) -> None:
        HttpRequest.__init__(self, req)

    @property
    def http_version(self) -> str:
        return self.method

    @property
    def status_code(self) -> int:
        return int(self.path)

    @property
    def reason(self) -> str:
        return self._HttpRequest__http_version.title()

    def is_valid(self) -> bool:
        return self.headers["Content-Length"] == len(self.body)

    def json(self) -> dict | None:
        if self.headers["Content-Type"] == "application/json":
            try:
                self.__json = json.loads(self.body)
            except Exception:
                return None
            return self.__json
