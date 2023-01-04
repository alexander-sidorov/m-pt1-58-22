import json
from typing import Any


class UrlParser:
    def __init__(self, body: str):
        self.__body = body
        self.__splitter()

    def __str__(self) -> str:
        return self.__body

    def __splitter(self) -> dict:  # CCR001
        self.scheme = None
        self.username = None
        self.password = None
        self.host = None
        self.port = None
        self.path = None
        self.query = None
        self.fragment = None

        def inner(st: str, splitter: str) -> tuple:
            if splitter in st:
                return tuple(st.split(splitter))
            return st, None

        self.scheme, temp_str = self.__body.split("://")
        if "?" in temp_str:
            temp_str, query_frag = inner(temp_str, "?")
            self.query, self.fragment = inner(query_frag, "#")
        if "/" in temp_str:
            temp_str, path = temp_str.replace("/", " /", 1).split(" ")
            if path != "" and path != "/":
                self.path = path
        if "@" in temp_str:
            user_pass, temp_str = temp_str.split("@")
            self.username, self.password = inner(user_pass, ":")
        self.host, port = inner(temp_str, ":")
        if port:
            self.port = int(port)

        components: dict = {
            "scheme": self.scheme,
            "username": self.username,
            "password": self.password,
            "host": self.host,
            "port": self.port,
            "path": self.path,
            "query": self.query,
            "fragment": self.fragment,
        }
        return components


class HttpRequest:
    def __init__(self, request_str: str):

        self.__request = request_str
        self.headers: dict = {}
        self.__body_extractor()
        self.__splitter()
        self.__splitter_headers()

    def __body_extractor(self) -> None:
        self.body = None
        self.__request, is_body = self.__request.split("\n\n", 1)
        body_reform = is_body.strip()
        if len(body_reform) > 0:
            self.body = is_body.lstrip().rstrip()

    def __splitter(self) -> None:
        self.__request_list: list = self.__request.split("\n")
        self.method, self.path, self.http_version = self.__request_list[
            0
        ].split(" ")
        del self.__request_list[0]

    def __splitter_headers(self) -> None:
        for pair in self.__request_list:
            key, value = pair.split(":")
            self.headers[key.strip()] = value.strip()


class HttpResponse:
    def __init__(self, response_str: str):
        self.__response = response_str
        self.headers: dict = {}
        self.__body_extractor()
        self.__splitter()
        self.__splitter_headers()
        self.__is_json: bool = (
            self.headers["Content-Type"] == "application/json"
        )
        self.__is_content: bool = (
            self.headers["Content-Length"] == self.__body_len
        )

    def __body_extractor(self) -> None:
        self.body = None
        self.__body_len: int = 0
        self.__response, is_body = self.__response.split("\n\n", 1)
        body_reform = is_body.strip()
        if len(body_reform) > 0:
            self.body = is_body.lstrip().rstrip()
            self.__body_len = len(self.body)

    def __splitter(self) -> None:
        self.__response_list: list = self.__response.split("\n")
        self.http_version, status_code, self.reason = self.__response_list[
            0
        ].split(" ", 2)
        self.status_code = int(status_code)
        del self.__response_list[0]

    def __splitter_headers(self) -> None:
        for pair in self.__response_list:
            key, val = pair.split(":")
            if "Content-Length" in key:
                value = int(val)
                self.headers[key.strip()] = value
            else:
                self.headers[key.strip()] = val.strip()

    def is_valid(self) -> bool:
        if self.body and self.__is_content:
            return True
        return False

    def json(self) -> Any:
        if self.is_valid() and self.__is_json and self.body:
            try:
                return json.loads(self.body)
            except json.decoder.JSONDecodeError:
                return None
        else:
            return None
