def sort_Holland_flag(arr):
    p1 = 0
    p2 = 0
    p3 = len(arr) - 1
    while p2 <= p3:
        if arr[p2] == 0:
            t = arr[p1]
            arr[p1] = arr[p2]
            arr[p2] = t
            p1 += 1
            p2 += 1
        elif arr[p2] == 1:
            p2 += 1
        else:
            t = arr[p2]
            arr[p2] = arr[p3]
            arr[p3] = t
            p3 -= 1
    return arr
