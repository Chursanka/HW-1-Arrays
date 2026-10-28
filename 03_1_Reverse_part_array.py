def arr_reverse(arr, l, r):
    while (l < r):
        t = arr[l]
        arr[l] = arr[r]
        arr[r] = t
        l += 1
        r -= 1

def part_reverse_arr(arr, k):
    n = len(arr)
    if n == 0:
        return arr
    k = k % n
    arr_reverse(arr, 0, n-1)
    arr_reverse(arr, 0, k-1)
    arr_reverse(arr, k, n-1)
    return arr

# Дополнительных аллокаций нет, так как функция arr_reverse изменяет текущий массив, а не добалвяет новый
# n\2 (первый вызов функции) + k\2 (второй) + (n-k)\2 (третий) операций "swap" элементов, следовательно при n -> бесконечность сложность = O(n) 
