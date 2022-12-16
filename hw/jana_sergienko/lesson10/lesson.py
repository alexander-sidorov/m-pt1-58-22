class User:
    pass
    def __int__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def get_class_name(self) -> str:
        return User.__name__

    def get_hollow_world(self) -> str:
        return "Hello world"
