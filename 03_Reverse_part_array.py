def arr_reverse(arr):
    l = 0
    r = len(arr) - 1
    while (l < r):
        t = arr[l]
        arr[l] = arr[r]
        arr[r] = t
        l += 1
        r -= 1
    return arr

def part_reverse_arr(arr, k):
    n = len(arr)
    k = k % n
    a = arr_reverse(arr)
    b = arr_reverse(a[:k])
    c = arr_reverse(a[k:])
    return b + c
