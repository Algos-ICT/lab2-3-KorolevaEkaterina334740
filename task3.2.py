from math import inf


def merge(arr: list, p: int, q: int, r: int):
    arr.insert(0, -inf)
    n1 = q - p + 1
    n2 = r - q
    left = [-inf]
    right = [-inf]
    for i in range(1, n1+1):
        left.append(arr[p+i-1])
    for j in range(1, n2+1):
        right.append(arr[q+j])
    left.append(inf)
    right.append(inf)
    i, j = 1, 1
    for k in range(p, r+1):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1
    del arr[0]
    print(p, r, arr[p-1], arr[r-1])


def merge_sort(a, p=None, r=None):
    if p is None:
        p = 1
    if r is None:
        r = len(a)
    if p >= r:
        return a
    q = (p + r)//2
    merge_sort(a, p, q)
    merge_sort(a, q+1, r)
    merge(a, p, q, r)
    return a


print(merge_sort([1, 8, 2, 1, 4, 7, 3, 2, 3, 6]))