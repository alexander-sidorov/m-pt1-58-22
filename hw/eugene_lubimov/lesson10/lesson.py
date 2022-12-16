class User:
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def get_name(self) -> str:
        return self._name

    @classmethod
    def get_class_name(cls) -> str:
        return cls.__name__

    def get_hello_world(self) -> str:
        return "hello world"


class Counter:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end
        self.num = start - 1

    def next(self) -> int:  # noqa: A003
        if self.num < self.end:
            self.num += 1
            return self.num
        return self.num