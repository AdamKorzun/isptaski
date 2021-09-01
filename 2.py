from math import factorial as fact

def A(n, k):
    return fact(n)//fact(n-k)

def genA(n):
    for i in range(n+1):
        yield A(n, i)

for i in genA(5):
    print(i)
