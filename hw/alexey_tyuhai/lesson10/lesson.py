import json
from typing import Any


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
        data = {"name": self.name}
        return json.dumps(data)

    def save_json(self, func_json: Any) -> Any:
        with open("data.json", "w") as g:
            g.write(func_json)


class Counter:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __iter__(self) -> "Counter":
        return self

    def __next__(self) -> int:
        if self.start < self.end:
            num = self.start
            self.start += 1
            return num
        raise StopIteration
