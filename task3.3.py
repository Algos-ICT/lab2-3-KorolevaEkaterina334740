from collections import deque
from math import inf


def merge_sort(arr):
    global count
    length = len(arr)
    if length == 1:
        return arr
    mid = length // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    left = deque(left)
    right = deque(right)
    i = len(left)
    j = len(right)
    left.append(inf)
    right.append(inf)
    arr = []
    while i > 0 or j > 0:
        if left[0] <= right[0]:
            arr.append(left.popleft())
            i -= 1
        else:
            arr.append(right.popleft())
            j -= 1
            if len(left) > 1:
                count += len(left) - 1
    return arr


count = 0
a = [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]
a = merge_sort(a)
print(count)