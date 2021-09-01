import random

l = 13
rng = (1, 20)

arr = random.sample(range(*rng), l)
print(arr)

def merge_sort(arr):
    l = len(arr)

    if len(arr) == 1:
        return arr
    elif len(arr) == 2:
        return sorted(arr)
    
    left = merge_sort(arr[:l//2])
    right = merge_sort(arr[l//2:])

    # [1, 2, 4, 8], [1, 3, 9, 27]

    res = []

    len_left, len_right = len(left), len(right)
    i, j = 0, 0

    while i < len_left and j < len_right:
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len_left:
        res.append(left[i])
        i += 1
    while j < len_right:
        res.append(right[j])
        j += 1

    return res

arr = merge_sort(arr)
print(arr)