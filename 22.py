from types import FunctionType

def dec(func, cond):
    if (not isinstance(func, FunctionType)) \
            or (not isinstance(cond, FunctionType)):
        raise ValueError()

    def nfunc(*args, **kwargs):
        s_args = sorted(args, key=cond)
        s_kwargs = {}
        
        for i in sorted(kwargs, key=lambda x: cond(kwargs[x])):
            s_kwargs[i] = kwargs[i]

        return func(*s_args, **s_kwargs)
    return nfunc

def print_all(*args, **kwargs):
    print(*args, *kwargs)

print_all = dec(print_all, lambda x: abs(x))

print_all(-2, 23, -4, 1, 2, 3, 0, 2, aboba=3, pupa=-1, brr=2, biba=-0)
