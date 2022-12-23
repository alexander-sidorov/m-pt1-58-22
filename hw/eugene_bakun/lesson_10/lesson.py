class User:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def get_class_name(self) -> str:
        return User.__name__

    def get_hello_world(self) -> str:
        return "hello world"


    def __init__(self, start: int, finish: int):
        self.start = start
        self.finish = finish
        self.current: int | None = None
        self.current = self.start


    def next(self) -> int:  # noqa: A003
       if self.current is None:
          self.current = self.start

       if self.current > self.stop:
          return self.stop
