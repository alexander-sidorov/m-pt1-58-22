class User:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def get_class_name(self) -> str:
        return User.__name__

    def get_hello_world(self) -> str:
        return "hello world"


class Counter:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.number = start

    def next(self):
        number = self.start
        self.number += 1
        return self.number
