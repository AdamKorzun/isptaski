from math import factorial as fact

def P(n):
    return fact(n)

def generation_П(n):
    for i in range(n+1):
        yield P(i)

for i in generation_П(5):
    print(i)
