class User:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_name(self) ->str:
        return self.name

    @classmethod
    def get_class_name(cls) -> str:
        return cls.__name__

    def get_hello_world(self) -> str:
        return "hello world"
