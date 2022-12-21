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
        self.current = self.start
        self.stop = stop

    def __iter__(self) -> "Counter":
        return self

    def __next__(self) -> int:
        if self.current > self.stop:
            raise StopIteration
        else:
            current_temp, self.current = self.current, self.current + 1
            return current_temp

    def cursor(self, pointer: int) -> None:
        if pointer < 0:
            self.current = self.start
        else:
            self.current = self.start + pointer
