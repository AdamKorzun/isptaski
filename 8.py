class Node:
    def __init__(self, v = 0, n = None):
        self.v = v
        self.n = n

    def partition(head, x):
        from math import inf
        pre_head = Node(-inf, head)
        c = pre_head
        t = None

        while c.n:
            if c.n.v >= x:
                t = c
                break
            c = c.n

        if not t:
            return


        while c and c.n:
            if c.n.v < x:
                t.n = Node(c.n.v, t.n)
                c.n = c.n.n
                t = t.n
                continue
            c = c.n
        
        return pre_head.n
        
#               t     c
values = [3, 1, 2, 1, 3, 5, 2, 5, 8, 2, 3, 2, 1, 5]
x = 3
head = Node()

c = head
for i in values:
    c.v = i

    if not c.n:
        c.n = Node()
    
    pre_c = c
    c = c.n
pre_c.n = None

values = []

c = head
while c:
    values.append(c.v)
    c = c.n

print(values)
head = head.partition(x)

res = []

c = head
while c:
    res.append(c.v)
    c = c.n

print(values)
print(res)
