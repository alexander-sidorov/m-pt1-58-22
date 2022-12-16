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
