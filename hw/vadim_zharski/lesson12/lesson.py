class UrlParser:
    def __init__(self, body: str):
        self.__body = body

    def __str__(self):
        return self.__body

    def splitter(self) -> dict:

        def inner(st: str, spl) -> tuple:
            if spl in st:
                return tuple(st.split(":"))
            return st, None

        self.__body.replace(" ", "")
        tempstr = self.__body.replace('://', " ").replace("@", " ").replace("/", " /", 1).split(" ")
        user, namepass = inner(tempstr[1], ":")
        host, port = inner(tempstr[2], ":")
        if "?" in tempstr[3]:
            path, suffix = tempstr[3].split('?')
            if '#' in suffix:
                query, fragm = suffix.split('#')
            else:
                query, fragm = suffix, None
        else:
            path, query, fragm = tempstr[3], None, None

        components = {
            "scheme": tempstr[0],
            "user": user,
            "password": namepass,
            "host": host,
            "port": port,
            "path": path,
            "query": query,
            "fragment": fragm,
        }
        return components


class Request:

    def __init__(self, method, path: str, version: str, headers: dict, body: str):
        self.__method = method
        self.__path = path
        self.__version = version
        self.__headers = headers
        self.__body = body


def main():
    test_url = UrlParser("http://user:password@host:1234/resourse")
    next_url = UrlParser("vnc://user:pass@localhost:8000/s/cree/n1?q=2#x")
    print(str(next_url))
    print(next_url.splitter())


if __name__ == "__main__":
    main()
