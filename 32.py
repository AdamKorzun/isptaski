nested_list = [[1, [1, 3]], 2, [1, 2, [6]]]

class nested_list_iter():
    def __init__(self, lst):
        self.iterable = lst[:]
        self.current = [0]

    def __iter__(self):
        return self

    def __next__(self):
        dpth = 1
        o = self.iterable
        
        for c in self.current:
            if isinstance(o[c], list):
                dpth += 1
                if dpth > len(self.current):
                    self.current.append(0)
                o = o[c]
            else:
                self.current[-1] += 1

            if self.current[-1] >= len(o):
                self.current = self.current[:-1]
                self.current[-1] += 1
                if self.current[0] >= len(self.iterable):
                    raise StopIteration()
                break

        return o[c]

def main():
    iter = nested_list_iter(nested_list)
    
    print(nested_list)
    while True:
        try:
            print(next(iter), end=' ')
        except StopIteration:
            break
    print()

