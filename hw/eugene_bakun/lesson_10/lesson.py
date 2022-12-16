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
    def __init__(self, start: int, finish: int):
        self.start = start
        self.finish = finish
        self.current: int | None = None
    def  next (self) -> int:
        self.start == 10
        self.finish == 11

        result, self.current = self.current, self.current +1
        return result

    
