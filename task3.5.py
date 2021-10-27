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

def major_exist(arr: list) -> bool:
    arr = merge_sort(arr)
    length = len(arr)
    mid = length // 2
    left = arr.index(arr[mid])
    right = length - arr[::-1].index(arr[mid]) - 1
    if right - left + 1 > length/2:
        return True
    return False


# n = int(input())
a = list(map(int, input().split()))
print(int(major_exist(a)))