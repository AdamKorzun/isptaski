from math import factorial as fact

def C(n, m):
    return fact(n)//fact(m)//fact(n-m)

def genC(n):
    for i in range(n+1):
        yield C(n, i)

for i in genC(3):
    print(i)