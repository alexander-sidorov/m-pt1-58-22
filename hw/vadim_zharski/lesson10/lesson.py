class User:

    __hello_world: str = "hello world"

    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name

    def get_class_name(self) -> str:
        return User.__name__

    def get_hello_world(self) -> str:
        return self.__hello_world

    def to_json(self) -> str:
        ret_str = '{"name":"%s"}' % self.name  # noqa: MOD001, S001
        return ret_str


class Counter:
    def __init__(self, start_pos: int, final_pos: int):
        self.__start_pos = start_pos
        self.__final_pos = final_pos
        self.__result = start_pos

    def __iter__(self) -> "Counter":
        return self

    def __next__(self) -> int:  # noqa: A003
        if self.__result < self.__final_pos:
            self.__result = self.__result + 1
            return self.__result
        raise StopIteration
