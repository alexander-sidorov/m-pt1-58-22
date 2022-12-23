def task_01_urlsplit(url: str) -> dict:  # noqa: CCR001
    url_dict: dict[str, str | int] = {}
    scheme = url[: url.find("://")]
    url_dict.update({"scheme": scheme})
    url = url[url.find("://") + 3:]
    user_data = url[: url.find("@")]
    if ":" in user_data:
        user_login = user_data[: user_data.find(":")]
        user_password = user_data[user_data.find(":") + 1:]
        url_dict.update({"user": user_login, "password": user_password})
    else:
        user_login = user_data
        url_dict.update({"user": user_login})
    url = url[url.find("@") + 1:]
    host_data = url[: url.find("/")]
    if ":" in host_data:
        port = host_data[host_data.find(":") + 1:]
        host = host_data[: host_data.find(":")]
        url_dict.update({"port": int(port), "host": host})
    else:
        host = host_data
        url_dict.update({"host": host})
    if "/" in url:
        if "?" in url:
            path = url[url.find("/"): url.find("?")]
            if "#" in url:
                query = url[url.find("?") + 1: url.find("#")]
                fragment = url[url.find("#") + 1:]
                url_dict.update({
                    "query": query,
                    "fragment": fragment,
                    "path": path
                })
            else:
                query = url[url.find("?") + 1:]
                url_dict.update({"query": query, "path": path})
        elif "#" in url:
            path = url[url.find("/"): url.find("#")]
            fragment = url[url.find("#") + 1:]
            url_dict.update({"path": path, "fragment": fragment})
        else:
            path = url
            url_dict.update({"path": path})
    else:
        pass
    return url_dict

class Request:
    def __init__(self, req: str):
        self.rq = req
        self.headers_dict = {}
        self.body = None
    def request_to_dict(self):
        req = self.rq
        headers = req.splitlines()
        head_tup = tuple(headers[0].split())
        self.method, self.path, self.version = head_tup
        headers.remove(headers[0])
        for header in headers:
            head = header.partition(": ")
            self.headers_dict.update({head[0]: head[2]})
        return None

f=Request(
    """GET /alexander-sidorov/m-pt-1-58-22 HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: github.com
User-agent: HTTPie/3.2.1
""")
f.request_to_dict()
print(f.headers_dict)
