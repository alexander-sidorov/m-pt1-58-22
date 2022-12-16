class User:
    pass

    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def get_class_name(self) -> str:
        return User.__name__

    def get_hello_world(self) -> str:
        return "hello world"


class Counter:
    pass

    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def next(self) -> int:
        start = 10
        end = 20
        while start < end:
            start += 1
        return start
