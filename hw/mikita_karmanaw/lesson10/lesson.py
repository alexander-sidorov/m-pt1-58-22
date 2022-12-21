class User:
    name = "User"

    def __init__(self, name: str) -> None:
        self.name = name

    def get_user_name(self) -> str:
        return self.name

    def get_class_name(self) -> str:
        return User.name

    def __str__(self) -> str:
        return User.name

    def get_hello_world(self) -> str:
        return "hello world"


class Counter:
    def __init__(self, start: int, stop: int) -> None:
        self.start = start
        self.stop = stop
        self.count = int(-1)

    def next(self) -> int:  # noqa: A003
        if self.count + self.start >= self.stop:
            return self.stop
        else:
            self.count += 1
            return self.count + self.start
