import random

l = 13
rng = (1, 20)
arr = random.sample(range(*rng), l)

print(arr)

def q_sort(arr):
    def partition(left, right):
        index = random.randint(left, right)
        pivot = arr[index]

        while left < right:
            while left < l and arr[left] <= pivot:
                left += 1
            while arr[right] > pivot:
                right -= 1
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
        
        arr[right], arr[index] = arr[index], arr[right]
        return right

    def sort(left, right):
       if left < right:
           p = partition(left, right)
           sort(p + 1, right)
           sort(left, p - 1)
    
    sort(0, l-1)
        
q_sort(arr)
print(arr)    


