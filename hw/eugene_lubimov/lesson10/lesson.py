class User:
    def __init__(self, name: str) -> None:
        self._name = name

    @classmethod
    def get_class_name(cls) -> str:
        return cls.__name__

    def get_hello_world(self) -> str:
        return "hello world"

    def __str__(self) -> str:
        return self._name


class Counter:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end
        self.num = start - 1

    def __iter__(self) -> "Counter":
        return self

    def __next__(self) -> int:  # noqa: A003
        if self.num < self.end:
            self.num += 1
            return self.num
        raise StopIteration
