class User:
    class_name = 'User'

    def __init__(self, nm):
        User.name = nm

    @classmethod
    def get_user_name(cls):
        return User.name

    @staticmethod
    def get_class_name():
        return User.class_name

    @staticmethod
    def get_hello_world():
        return "hello world"
