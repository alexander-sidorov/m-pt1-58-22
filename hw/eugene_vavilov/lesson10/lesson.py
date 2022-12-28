import json


class User:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name

    def get_class_name(self) -> str:
        return User.__name__

    def get_hello_world(self) -> str:
        return "hello world"

    def to_json(self) -> str:
        js = json.dumps({"name": self.name})
        return str(js)


class Counter:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end
        self.number = start - 1

    def __iter__(self) -> "Counter":
        return self

    def __next__(self) -> int:  # noqa A003
        if self.start <= self.end:
            num = self.start
            self.start += 1
        else:
            raise StopIteration
        return num
