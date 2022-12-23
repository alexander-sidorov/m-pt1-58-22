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
