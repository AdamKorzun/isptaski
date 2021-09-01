def cache(size):
    def cached(func):
        cache = {}
        def wrapper(*args, **kwargs):
            if len(cache) >= size:
                return func(*args, **kwargs)

            arg = (bytes(args), bytes(kwargs))
            if arg not in cache:
                cache[arg] = func(*args, **kwargs)
            return cache[arg]
        return wrapper
    return cached


@cache(10)
def square(x):
    return x*x

for i in range(11):
    print(square(i))
