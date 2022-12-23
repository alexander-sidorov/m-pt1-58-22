from urllib.parse import urlparse


def task_01_urlsplit(url: str) -> dict:
    dict_url = urlparse(url)
    netloc = dict_url[1]
    netloc_dict = {
        "user": netloc[: netloc.find(":")],
        "password": netloc[netloc.find(":") + 1: netloc.find("@")],
        "host": netloc[netloc.find("@") + 1: -5],
        "port": netloc[-4:],
    }
    dict_url1 = {
        "scheme": dict_url[0],
        "path": dict_url[2],
        "query": dict_url[4],
        "fragment": dict_url[5],
    }
    all_dict = dict_url1 | netloc_dict
    return all_dict
