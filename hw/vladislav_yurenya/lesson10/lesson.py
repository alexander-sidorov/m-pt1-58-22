class User:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}"

    def get_class_name(self) -> str:
        return User.__name__

    def get_hello_world(self) -> str:
        return "hello world"


class Counter:
    def __init__(self, start: int, stop: int):
        self.start = start
        self.stop = stop
        self.resault = self.start - 1

    def next(self) -> int:  # noqa: A003
        self.resault += 1
        return self.resault
