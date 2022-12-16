class User:
    def __init__(self,name):
        self.name = name
    def get_name(self):
        return self.name

    def get_class_name(self):
        return User.__name__
    
    def get_hello_world(self):
        return "hello world"

class Counter:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = self.start
  
    def next(self)-> int:
        if self.current > self.end:
            return self.end
        result, self.current = self.current, self.current + 1
        return result



