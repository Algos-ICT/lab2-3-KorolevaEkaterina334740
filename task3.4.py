def binary_search(arr, x, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    if right < left:
        return -1
    mid = (right - left) // 2 + left
    if mid >= len(arr):
        return -1
    if x == arr[mid]:
        return mid
    elif x < arr[mid]:
        return binary_search(arr, x, left=left, right=mid - 1)
    else:
        return binary_search(arr, x, left=mid + 1, right=right)


n = int(input())
a = sorted(map(int, input().split()))
k = int(input())
for i in map(int, input().split()):
    print(binary_search(a, i), end=' ')