import json


class Url:
    def __init__(self, url: str) -> None:  # noqa: CCR001
        self.scheme: None | str = None
        self.username: None | str = None
        self.password: None | str = None
        self.host: None | str = None
        self.port: None | int = None
        self.path: None | str = None
        self.query: None | str = None
        self.fragment: None | str = None
        self.scheme = url[: url.find("://")]
        url_without_scheme = url[url.find("://") + 3:]  # noqa: BLK100
        if ("/" in url_without_scheme) or (
            ("?" in url_without_scheme) and ("/" not in url_without_scheme)
        ):
            try:
                access_data = url_without_scheme[
                    : url_without_scheme.index("/")
                ]
                request_data = url_without_scheme[
                    url_without_scheme.index("/"):
                ]
            except ValueError:
                access_data = url_without_scheme[
                    : url_without_scheme.index("?")
                ]
                request_data = url_without_scheme[
                    url_without_scheme.index("?"):
                ]
            if "#" in request_data:
                self.fragment = request_data[request_data.find("#") + 1:]
                request_data = request_data[: request_data.find("#")]
            else:
                pass
            if "?" in request_data:
                self.query = request_data[request_data.find("?") + 1:]
                request_data = request_data[: request_data.find("?")]
            else:
                pass
            self.path = request_data
            if self.path == "":
                self.path = None
        else:
            access_data = url_without_scheme
        if "@" in access_data:
            user_data = access_data[: access_data.find("@")]
            host_data = access_data[access_data.find("@") + 1:]
            if ":" in user_data:
                self.username = user_data[: user_data.find(":")]
                self.password = user_data[user_data.find(":") + 1:]
            else:
                self.username = user_data
        else:
            host_data = access_data
        if ":" in host_data:
            self.host = host_data[: host_data.find(":")]
            self.port = int(host_data[host_data.find(":") + 1:])
        else:
            self.host = host_data


class HttpRequest:
    def __init__(self, req: str) -> None:
        self.method: None | str = None
        self.path: None | str = None
        self.http_version: None | str = None
        self.headers: dict[str, str] = {}
        self.body: None | str = None
        self.body = req[req.find("\n\n") + 2:]
        if self.body == "":
            self.body = None
        req = req[: req.find("\n\n")]
        lines = req.splitlines()
        head = lines[0].split(" ")
        self.method, self.path, self.http_version = head[0], head[1], head[2]
        del lines[0]
        for line in lines:
            header = line.split(": ")
            self.headers.update({header[0]: header[1]})


class HttpResponse:
    def __init__(self, resp: str) -> None:
        self.status_code: None | int = None
        self.reason: None | str = None
        self.http_version: None | str = None
        self.headers: dict[str, str | int] = {}
        self.body: None | str = None
        self.body = resp[resp.find("\n\n") + 2:]
        if self.body == "":
            self.body = None
        resp = resp[: resp.find("\n\n")]
        lines = resp.splitlines()
        head = lines[0]
        self.http_version = head.partition(" ")[0]
        head = head[len(self.http_version) + 1:]
        code = head.partition(" ")[0]
        self.status_code = int(code)
        self.reason = head[len(code) + 1:].title()
        del lines[0]
        for line in lines:
            header = line.split(": ")
            if header[1].isdigit():
                header[1] = int(header[1])  # noqa: [call-overload]
            self.headers.update({header[0]: header[1]})

    def is_valid(self) -> bool:
        return len(self.body) == self.headers["Content-Length"]  # noqa: [arg-type]

    def json(self) -> dict | None:
        if "json" in self.headers["Content-Type"]:  # noqa: [operator]
            return json.loads(self.body)  # noqa: [no-any-return], [arg-type]
        else:
            return None
