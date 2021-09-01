def few_times(n):
    def repeater(func):
        def wrapper(*args, **kwargs):
            res = []
            for i in range(n):
                res.append(func(*args, **kwargs))
            return tuple(res)
        return wrapper
    return repeater

@few_times(3)
def a():
    print('boo')

print(a())