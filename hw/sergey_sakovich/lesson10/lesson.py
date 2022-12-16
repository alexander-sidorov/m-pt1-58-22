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

    def next(self):

        if self.start < self.end:
            self.start += 1
            return self.start
        else:
            print("Всё")
