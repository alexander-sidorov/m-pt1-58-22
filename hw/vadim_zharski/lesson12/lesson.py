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
        self.headers: dict = {}
        for pair in self.__request_list:
            key, value = pair.split(":")
            self.headers[key.strip()] = value.strip()


class HttpResponse:
    def __init__(self, response: str):
        self.__response = response
        self.__body_extractor()
        self.__response_list: list = self.__response.split('\n')
        self.__splitter()
        self.__splitter_headers()

    def __body_extractor(self) -> None:
        self.body = None
        self.__response, is_body = self.__response.split("\n\n", 1)
        body_reform = is_body.strip()
        if len(body_reform) > 0:
            self.body = is_body.lstrip().rstrip()

    def __splitter(self) -> None:
        self.http_version, status_code, self.reason = self.__response_list[0].split(' ', 2)
        self.status_code = int(status_code)
        del (self.__response_list[0])

    def __splitter_headers(self) -> None:
        self.headers: dict = {}
        for pair in self.__response_list:
            key, val = pair.split(':')
            if "Content-Length" in key:
                value = int(val)
                self.headers[key.strip()] = value
            else:
                self.headers[key.strip()] = val.strip()

    def is_valid(self) -> bool:
        if self.body:
            if self.headers["Content-Length"] == len(self.body):
                return True
        return False

    def json(self) -> Any:
        __json_obj = None
        if self.is_valid() and self.headers["Content-Type"] == "application/json":
            try:
                __json_obj = json.loads(self.body)
                return __json_obj
            except json.decoder.JSONDecodeError:
                return __json_obj
        else:
            return __json_obj


def main():
    message = """HTTP/1.1 404 NOT FOUND
    Content-Length: 48
    Content-Type: text/html
    Server: gunicorn/19.9.0

    {"status_code": 404, "description": "no access"}
    """

    resp = HttpResponse(message)

    assert resp.is_valid()
    assert resp.json() is None
    printer(resp)
    print(resp.json())


def printer(obj: HttpResponse) -> None:
    print(f"{obj.status_code}\n{obj.reason}\n{obj.http_version}\n{obj.headers}\n{obj.body}")


if __name__ == "__main__":
    main()
