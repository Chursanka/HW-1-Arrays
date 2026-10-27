# Задача - "Тwo sum"
def two_sum (arr, target):
    l = 0
    r = len(arr) - 1
    s = arr[l] + arr[r]
    while (s != target):
        if s > target:
            r -= 1
        else:
            l += 1
        s = arr[l] + arr[r]
    return [l, r]
