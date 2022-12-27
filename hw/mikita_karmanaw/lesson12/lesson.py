import json
from typing import Any
from typing import cast


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
        url_scheme_pos = url.find("://")
        self.scheme = url[:url_scheme_pos]
        scheme_cut_pos = url_scheme_pos + 3
        url_no_scheme = url[scheme_cut_pos:]
        if ("/" in url_no_scheme) or (
            ("?" in url_no_scheme) and ("/" not in url_no_scheme)
        ):
            try:
                cut_request_pos = url_no_scheme.index("/")
                access_data = url_no_scheme[:cut_request_pos]
                request_data = url_no_scheme[cut_request_pos:]
            except ValueError:
                cut_request_pos = url_no_scheme.index("?")
                access_data = url_no_scheme[:cut_request_pos]
                request_data = url_no_scheme[cut_request_pos:]
            if "#" in request_data:
                frag_pos = request_data.find("#")
                frag_cut_pos = frag_pos + 1
                self.fragment = request_data[frag_cut_pos:]
                request_data = request_data[:frag_pos]
            if "?" in request_data:
                query_pos = request_data.find("?")
                query_cut_pos = query_pos + 1
                self.query = request_data[query_cut_pos:]
                request_data = request_data[:query_pos]
            self.path = request_data
            if self.path == "":
                self.path = None
        else:
            access_data = url_no_scheme
        if "@" in access_data:
            host_pos = access_data.find("@")
            host_cut_pos = host_pos + 1
            user_data = access_data[:host_pos]
            host_data = access_data[host_cut_pos:]
            if ":" in user_data:
                pass_pos = user_data.find(":")
                pass_cut_pos = pass_pos + 1
                self.username = user_data[:pass_pos]
                self.password = user_data[pass_cut_pos:]
            else:
                self.username = user_data
        else:
            host_data = access_data
        if ":" in host_data:
            port_pos = host_data.find(":")
            port_cut_pos = port_pos + 1
            self.host = host_data[:port_pos]
            self.port = int(host_data[port_cut_pos:])
        else:
            self.host = host_data


class HttpRequest:
    def __init__(self, req: str) -> None:
        self.method: None | str = None
        self.path: None | str = None
        self.http_version: None | str = None
        self.headers: dict[str, str] = {}
        self.body: None | str = None
        body_cut_pos = req.find("\n\n") + 2
        self.body = req[body_cut_pos:]
        if self.body == "":
            self.body = None
        req = req[: req.find("\n\n")]
        lines = req.splitlines()
        head = lines[0].split(" ")
        self.method, self.path, self.http_version = head
        del lines[0]
        for line in lines:
            header = line.split(": ")
            self.headers[header[0]] = header[1]


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
