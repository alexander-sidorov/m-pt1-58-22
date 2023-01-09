class Url:
    def get_schema(url: str) -> dict:
        dict_url = {}
        new_url = url

        schema = url.split("://")[0]
        dict_url.update({"schema": schema})

        user = url.split(":")[1].replace("//", "")
        dict_url.update({"user:": user})

        password = url.split(":")[2].split("@")[0]
        dict_url.update({"password": password})

        host = url.split(":")[2].split("/")[0]
        dict_url.update({"host": host})

        port = url.split(":")[3].split("/")[0]
        dict_url



