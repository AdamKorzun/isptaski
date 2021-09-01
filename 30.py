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

class tree_iter():
    def __init__(self, node: Node):
        self.root = node
        self.path = [] # 'l' - left, 'r' - right        
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.path and self.path[0] == 'end':
            raise StopIteration()

        c = self.root

        if not self.path:
            while c.l:
                c = c.l
                res = c.v
                self.path.append('l')
            if c.r:
                c = c.r
                self.path.append('r')

                while c.l:
                    c = c.l
                    self.path.append('l')
            else:
                self.path = self.path[:-1]
            if not self.path:
                self.path.append('root')
            return res
        
        if self.path[0] == 'root':
            self.path = []
            if c.r:
                c = c.r
                self.path.append('r')
                while c.l:
                    c = c.l
                    self.path.append('l')
            else:
                self.path.append('end')
            
            return self.root.v
        
        for i in self.path:
            c = c.__dict__[i]
        res = c.v
        
        if self.path[-1] == 'r':
            if c.r:
                c = c.r
                self.path.append('r')
                while c.l:
                    c = c.l
                    self.path.append('l')
            else:
                while self.path and self.path[-1] == 'r':
                    self.path = self.path[:-1]
                if self.path:
                    if self.path[-1] == 'l':
                        self.path = self.path[:-1]
                        if not self.path:
                            self.path.append('root')
                else:
                    self.path.append('end')
        else:
            if c.r:
                c = c.r
                self.path.append('r')
                while c.l:
                    c = c.l
                    self.path.append('l')
            else:
                self.path = self.path[:-1]
                if not self.path:
                    self.path.append('root')

        return res


rng = (10, 40)

root = Node(int(random.randint(*rng)))
for i in range(10):
    root += int(random.randint(*rng))

def main():
    root.print()
    iter = tree_iter(root)
    while True:
        try:
            print(next(iter), end=' ')
        except StopIteration:
            break
        except Exception as msg:
            print(msg)
            break

main()
