class User:
    class_name = 'User'

    def __init__(self, nm) -> None:
        User.name = nm

    @classmethod
    def get_user_name(cls) -> str:
        return User.name

    @staticmethod
    def get_class_name() -> str:
        return User.class_name

    @staticmethod
    def get_hello_world() -> str:
        return "hello world"
