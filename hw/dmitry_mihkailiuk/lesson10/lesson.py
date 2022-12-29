import json
from typing import Any
from pathlib import Path


class User:
    def __init__(self, name: str) -> None:
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

    def save_json(self, destination: str | Path) -> Any:
        json_file = Path(destination)
        with json_file.open("w") as stream:
            json.dump({"name": self.name}, stream)


class Counter:
    def __init__(self, start: int, stop: int) -> None:
        self.start = start
        self.stop = stop

    def __iter__(self) -> "Counter":
        return self

    def __next__(self) -> int:
        if self.start < self.stop:
            num = self.start
            self.start += 1
            return num
        raise StopIteration
