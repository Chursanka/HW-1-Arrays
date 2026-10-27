def even_d_forward(arr):
    left = 0
    for cur in range(len(arr)):
        if arr[cur] % 2 == 0:
            t = arr[left]
            arr[left] = arr[cur]
            arr[cur] = t
            left += 1
    return arr
# Порядок четных чисел сохраняется за счет индекса left: последнее встреченное четное число добавляем в конец "подмассива" четных чисел    
