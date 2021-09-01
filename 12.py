import random

class Node:
    def __init__(self, v = 0, l = None, r = None):
        self.v = v
        self.l = l
        self.r = r

    def print(self, indent = 4, depth = 0):
        if self.r is not None:
            (self.r).print(indent, depth + 1)
        print(' ' * depth * indent, self.v)
        if self.l is not None:
            (self.l).print(indent, depth + 1)

    def __add__(self, v):
        c = self

        while True:
            if v > c.v:
                if c.r:
                    c = c.r
                else:
                    c.r = Node(v)
                    break
            elif v < c.v:
                if c.l:
                    c = c.l
                else:
                    c.l = Node(v)
                    break
            else:
                break

        return self

    def height(self):
        r = self.r.height() if self.r else 0
        l = self.l.height() if self.l else 0

        res = (r if r > l else l) + 1
        return res


rng = (10, 40)

root = Node(int(random.randint(*rng)))
for i in range(10):
    root += int(random.randint(*rng))

root.print()
print(root.height())
