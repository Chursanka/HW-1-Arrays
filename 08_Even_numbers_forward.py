def even_d_forward(arr):
    left = 0
    for cur in range(len(arr)):
        if arr[cur] % 2 == 0:
            t = arr[left]
            arr[left] = arr[cur]
            arr[cur] = t
            left += 1
    return arr
