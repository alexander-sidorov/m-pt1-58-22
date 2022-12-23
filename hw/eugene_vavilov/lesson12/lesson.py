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

    ditail = url.split(separators[0], maxsplit=1)
    schema[syntax_name[0]] = ditail[0]
    url = ditail[1]
    last_separator = 1

    if "@" in url:
        ditail = url.split(separators[1], maxsplit=1)
        schema[syntax_name[1]] = ditail[0]
        url = ditail[1]

        ditail = url.split(separators[2], maxsplit=1)
        schema[syntax_name[2]] = ditail[0]
        url = ditail[1]
        last_separator = 3
    if ":" in url:
        ditail = url.split(separators[3], maxsplit=1)
        schema[syntax_name[3]] = ditail[0]
        url = ditail[1]
        last_separator = 4

    if "/" in url:
        ditail = url.split(separators[4], maxsplit=1)
        schema[syntax_name[4]] = ditail[0]
        url = ditail[1]
        last_separator = 5

    if "?" in url:
        ditail = url.split(separators[5], maxsplit=1)
        schema[syntax_name[5]] = ditail[0]
        url = ditail[1]
        last_separator = 6

    if "#" in url:
        ditail = url.split(separators[6], maxsplit=1)
        schema[syntax_name[6]] = ditail[0]
        url = ditail[1]
        last_separator = 7

    schema[syntax_name[last_separator]] = url


    return schema

print(task_01_urlsplit("https://github.com/alexander-sidorov/m-pt1-58-22/pulls"))