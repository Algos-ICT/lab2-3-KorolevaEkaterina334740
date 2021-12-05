from math import inf
from collections import deque
from time import perf_counter


def merge_sort(arr):
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
        if left[0] < right[0]:
            arr.append(left.popleft())
            i -= 1
        else:
            arr.append(right.popleft())
            j -= 1
    return arr


if __name__ == '__main__':
    f = open('input.txt')
    a = list(map(int, f.readline().split()))
    start_time = perf_counter()
    a = merge_sort(a)
    end_time = perf_counter()
    print(end_time - start_time)