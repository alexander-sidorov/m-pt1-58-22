def task_01_urlsplit(url: str) -> dict:
    schema = {}
    separators = ["://", ":", "@", ":", "/", "?", "#"]
    syntax_name = [
        "scheme",
        "user",
        "password",
        "host",
        "port",
        "path",
        "query",
        "fragment",
    ]
    num = 0
    while num < 7:
        ditail = url.split(separators[num], maxsplit=1)
        schema[syntax_name[num]] = ditail[0]
        num += 1
        url = ditail[1]
    return schema
