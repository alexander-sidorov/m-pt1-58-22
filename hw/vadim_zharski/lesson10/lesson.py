class User:

    __hello_world: str = "hello world"

    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def get_class_name(self) -> str:
        return User.__name__

    def get_hello_world(self) -> str:
        return self.__hello_world


some_user = User("some_user")
print(some_user.get_name())
print(some_user.get_hello_world())

