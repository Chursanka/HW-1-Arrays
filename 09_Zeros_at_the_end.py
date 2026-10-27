def zero_back(arr):
    left = 0
    right = len(arr) - 1
    while arr[right] == 0:
        right -= 1
    cur = 0
    while cur < right:
        if arr[cur] == 0:
            t = arr[right]
            arr[right] = arr[cur]
            arr[cur] = t
            right -= 1
            while arr[right] == 0:
                    right -= 1
        else:
            cur += 1
    return arr
