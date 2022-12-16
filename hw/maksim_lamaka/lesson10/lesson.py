class User:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_name(self):
        return self.name

    def get_class_name(self):
        return User.__name__

    def