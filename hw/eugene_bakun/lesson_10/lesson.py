from typing import Optional
class User:

    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name

    def get_class_name(self) -> str:
        return User.__name__

    def get_hello_world(self) -> str:
        return "hello world"


class Counter:
    def __init__(self, start: int, stop: int):
        self.start = start
        self.stop = stop
        self.current: self.start

    def __iter__(self) -> "Counter":
        return self


    def __next__(self) -> int:
        if self.current > self.stop:
            raise StopIteration

        result, self.current = self.current, self.current + 1
        return result
