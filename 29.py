import re

file_path = '29.txt'

class MoreFields(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)

        with open(file_path) as f:
            file_content = f.read()
        field_pattern = '(\\w+) ?= ?(.+)\\s?'
        fields = re.findall(field_pattern, file_content)
        
        for (k, v) in fields:
            if v[0] == v[-1] and v[0] in '\'\"':
                v = v[1:-1]
            setattr(x, k, v)

        return x

class A(metaclass=MoreFields):
    pass

print(f'{A.field1 = }\n{A.field2 = }\n{A.aboba = }\n')
a = A()
print(f'{a.field1 = }\n{a.field2 = }\n{a.aboba = }')
