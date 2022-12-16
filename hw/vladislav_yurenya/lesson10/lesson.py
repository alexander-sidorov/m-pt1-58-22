class User:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def get_class_name(self) -> str:
        return User.__name__

    def get_hello_word(self) -> str:
        return "hello word"


class Counter:
    def __init__(self, start: int, stop: int):
        self.start = start
        self.stop = stop
        self.resault = self.start

    def next(self) -> int:  # noqa: A003
        if self.resault > self.stop:
            return self.stop
        result, self.resault = self.resault, self.resault + 1
        return result


c = Counter(10, 20)
