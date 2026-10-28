def zero_back(arr):
    cnt = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[w] = arr[i]
            w += 1
    for i in range(w, len(arr)):
        arr[i] = 0

# Сложность линейная, потому что в самом худшем случае программа
