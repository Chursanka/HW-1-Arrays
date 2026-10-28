def zero_back(arr):
    cnt = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[cnt] = arr[i]
            cnt += 1
    for i in range(cnt, len(arr)):
        arr[i] = 0

# Сложность линейная, потому что в самом худшем случае программа проходит по массиву два раза
