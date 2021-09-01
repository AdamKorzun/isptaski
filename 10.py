from numpy import asarray, zeros
import random

n = random.randint(4, 7)
m = random.randint(4, 7)

field = []

print(f'{n=}\n{m=}')

for i in range(n):
    field.append([])
    for j in range(m):
        field[i].append(int(random.randint(0, 1)))

print('field:\n', asarray(field))

def count_island(field):
    def erase_land(i, j): # aka global warming
        if i == -1 or i == n or j == -1 or j == m:
            return
        if not field[i][j]:
            return
        field[i][j] = 0
        erase_land(i + 1, j)
        erase_land(i - 1, j)
        erase_land(i, j + 1)
        erase_land(i, j - 1)

    res = 0
    for i in range(n):
        for j in range(m):
            if field[i][j]:
                res += 1
                erase_land(i, j)

    return res

res = count_island(field)
print(res)
