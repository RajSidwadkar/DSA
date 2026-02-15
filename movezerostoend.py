def movezerostoend(arr):
    
    n = len(arr)
    result = [0] * n

    i = j = 0
    for i in range(n):
        if arr[i] != 0:
            result[j] = arr[i]
            j += 1

    return result

        

print(movezerostoend([1,0,5,0,3,4,0,2]))

        


