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
        return json.dumps({"rabbit": self.name})


class Counter:
    def __init__(self, start: int, stop: int):
        self.start = start
        self.stop = stop
        self.resault = self.start - 1

    def __iter__(self) -> "Counter":
        return self

    def __next__(self) -> int:  # noqa: A003
        if self.stop - 1 < self.resault:
            raise StopIteration
        self.resault += 1
        return self.resault
