import json


class User:
    name = "User"

    def __init__(self, name: str) -> None:
        self.name = name

    def get_class_name(self) -> str:
        return User.name

    def __str__(self) -> str:
        return self.name

    def get_hello_world(self) -> str:
        return "hello world"

    def to_json(self) -> str:
        return json.dumps({"name": self.name})


class Counter:
    def __init__(self, start: int, stop: int) -> None:
        self.start = start
        self.stop = stop

    def __iter__(self) -> "Counter":
        return self

    def __next__(self) -> int:
        if self.start > self.stop:
            raise StopIteration
        else:
            start_temp, self.start = self.start, self.start + 1
            return start_temp
