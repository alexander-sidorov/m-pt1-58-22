from urllib.parse import urlparse


def pars_url(url: str) -> dict:
    pars = urlparse(url)
    return {
        "scheme": pars.scheme,
        "user": pars.username,
        "password": pars.password,
        "host": pars.hostname,
        "port": pars.port,
        "path": pars.path,
        "query": pars.query,
        "fragment": pars.fragment,
    }


class Request:
    def __init__(self, req: str) -> None:
        self.req = req.split("\n")

    def method(self) -> str:
        return self.req[0].split()[0]

    def path(self) -> str:
        return self.req[0].split()[1]

    def version(self) -> str:
        return self.req[0].split()[2]

    def headers(self) -> dict:
        self.headers_dict: dict = {}
        for head in self.req[1:-3]:
            head1: list = head.split(": ")
            self.headers_dict[head1[0]] = head1[1]
        return self.headers_dict

    def body(self) -> str:
        return self.req[-1]


req = """HEAD /docs/python_3/library/urllib.parse.html HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: digitology.tech
User-Agent: HTTPie/3.2.1


"""
