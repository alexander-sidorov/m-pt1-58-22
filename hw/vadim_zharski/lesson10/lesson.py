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


class Counter:
    def __init__(self, start_pos: int, final_pos: int):
        self.__start_pos = start_pos
        self.__final_pos = final_pos
        self.__result = start_pos

    def next(self) -> int:  # noqa: A003
        if self.__result < self.__final_pos:
            self.__result = self.__result + 1
        return self.__result
