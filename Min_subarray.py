def min_sub_arr(arr, target):
    left = 0
    s = 0
    res = len(arr) + 1
    for right in range(len(arr)):
        s += arr[right]
        while s >= target:
            cur_len = right - left + 1
            if cur_len < res:
                res = cur_len
            s -= arr[left]
            left += 1
        right += 1
    if res == len(arr) + 1:
        res = 0
    return res
