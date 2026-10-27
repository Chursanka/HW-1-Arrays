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
