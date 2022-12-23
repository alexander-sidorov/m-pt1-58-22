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
