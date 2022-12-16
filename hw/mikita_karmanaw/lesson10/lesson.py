class User:
    name = "User"

    def __init__(self, nm: str) -> None:
        User.name = nm

    def get_user_name(self) -> str:
        return self.name

    def get_class_name(self) -> str:
        return User.__name__

    def get_hello_world(self) -> str:
        return "hello world"


class Counter:
    def __init__(self, start: int, stop: int) -> None:
        self.start = start
        self.stop = stop
        self.count = int(-1)
        return None

    def next(self) -> int | None:  # noqa: A003
        if self.count + self.start >= self.stop:
            pass
        else:
            self.count += 1
            return self.count + self.start
