import urllib.parse


def task_01_urlsplit(url: str) -> dict:
    base_url = 'http://user:password@host:1234/resourse'
    url_path = dict(urllib.parse.urlsplit(base_url))

    return url_path

