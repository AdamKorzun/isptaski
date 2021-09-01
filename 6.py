from math import factorial as fact

def A(n, k):
    return fact(n)//fact(n-k)

class iterA():
    def __init__(self, n):
        self.n = n
        self.m = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.m > self.n:
            raise StopIteration()
        
        self.m += 1

        return A(self.n, self.m - 1)

i = iter(iterA(5))

while True:
    try:
        print(next(i))
    except StopIteration:
        break