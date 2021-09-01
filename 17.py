class singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in singleton._instances:
            singleton._instances[cls] = super().__call__(*args, **kwargs)
        return singleton._instances[cls]

class A(metaclass=singleton):
    pass

a = A()
b = A()

print(f'{id(a) - id(b) = }')