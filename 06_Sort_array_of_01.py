def sort_01(arr):
    left = 0
    right = len(arr) - 1
    while (left < right):
        if (arr[left] == 1):
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1
        else:
            left += 1
    return arr

# В самом худшем случае цикл произведет n/2 "swap", что соответсвует сложности O(n)
