class Url:
    def get_url(url: str) -> dict:
        dict_url = {}
        new_url = url
        schema = url.split("://")[0]

        dict_url.update({"schema": schema})



