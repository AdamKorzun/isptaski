from typing import List, Tuple
interval = Tuple[int, int]

class intervals:
    def __init__(self):
        self._ints: List[interval] = []


    def __add__(self, i:interval):
        if i[0] != i[1]:
            self._ints.append(i)
            self._merge()
        return self


    def _merge(self):
        self._ints.sort(key=lambda x: x[0])

        l = len(self._ints)

        i = -1
        while (i:=i+1) < l - 1:
            c = self._ints[i]
            n = self._ints[i + 1]
            
            if c[0] == n[0]:
                if c[1] <= n[1]:
                    self._ints.pop(i)
                    i -= 1
                    l -= 1
                elif c[1] > n[1]:
                    self._ints.pop(i + 1)
                    i -= 1
                    l -= 1
            else:
                if c[1] >= n[1]:
                    self._ints.pop(i + 1)
                    i -= 1
                    l -= 1    
                elif c[1] > n[0]:
                    self._ints.insert(i, (c[0], n[1]))
                    self._ints.pop(i + 1)
                    self._ints.pop(i + 1)
                    i -= 1
                    l -= 1                

        # bla = []
        # for i in self._ints:
        #     bla.append((i[0], True))
        #     bla.append((i[1], False))

        # bla.sort(key = lambda x: x[0])

        # l = len(bla)
        # i = -1
        # while (i:=i+1) < l - 1:
        #     if bla[i][1] == bla[i+1][1]:
        #         if bla[i][1]:
        #             bla.pop(i+1)
        #         else:
        #             bla.pop(i)
        #         i -= 1
        #         l -= 1
        #     elif bla[i][0] == bla[i+1][0]:
        #         if bla[i][1] != bla[i+1][1]:
        #             bla.pop(i)
        #             l -= 1
        #         bla.pop(i)
        #         l -= 1
        #         i -= 1

        # self._ints = []
        # i = -2
        # while (i:=i+2) < l:
        #     self._ints.append((bla[i][0], bla[i+1][0]))


    def __repr__(self):
        return str(self._ints)

ints = intervals()
ints += (1, 3)
print(ints)
ints += (5, 6)
print(ints)
ints += (4, 7)
print(ints)
ints += (1, 2)
print(ints)
ints += (2, 8)
print(ints)