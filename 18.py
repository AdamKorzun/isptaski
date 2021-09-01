class singleton():
    _instances = {}
    def __new__(cls, *args, **kwargs):
        if cls not in singleton._instances:
            singleton._instances[cls] = object.__new__(cls)
            singleton._instances[cls].__init__(*args, **kwargs)
        return singleton._instances[cls]

class A(singleton):
    def __init__(self, a = 2, b = 3):
        self.a = a
        self.b = b

a = A()
b = A()

print(f'{id(a) - id(b)}')
