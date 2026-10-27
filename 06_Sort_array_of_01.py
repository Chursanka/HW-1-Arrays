def sort_01(arr):
    left = 0
    right = len(arr) - 1
    while left != right:
        if arr[right] == 1:
            right -= 1
        elif arr[left] == 0:
            left += 1
        else:
            t = arr[left]
            arr[left] = arr[right]
            arr[right] = t
            left += 1
            right -=1
    return arr
