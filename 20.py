import time

def expired_cache(t):
    def cached(func):
        cache = {}
        def wrapper(*args, **kwargs):
            arg = (bytes(args), bytes(kwargs))
            if (arg not in cache) or (time.time() - cache[arg][1] > t):
                cache[arg] = (func(*args, **kwargs), time.time())
            return cache[arg][0]
        return wrapper
    return cached


@expired_cache(10)
def square(x):
    time.sleep(1)
    return x*x

for i in range(1000):
    for j in range(100):
        t = time.time()
        print(square(j//10), i)
        print(time.time() - t, '\n')

