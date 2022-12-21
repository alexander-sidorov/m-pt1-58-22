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
        self.current = self.start

    def next(self) -> int:  # noqa: A003
        if self.current > self.stop:
            return self.stop

        result, self.current = self.current, self.current + 1
        return result

print(str(User("asdadadsd")))

