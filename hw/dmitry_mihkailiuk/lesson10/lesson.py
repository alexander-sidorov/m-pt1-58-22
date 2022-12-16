class User:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_class_name(self):
        return str(User.__name__)

    def get_hello_world(self):
        return "hello world"
