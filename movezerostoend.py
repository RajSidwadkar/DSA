def movezerostoend(arr):

    n = len(arr)
    
    # SC = O(N)
    # result = [0] * n
    # j = 0
    # for i in range(n):
    #     if arr[i] != 0:
    #         result[j] = arr[i]
    #         j += 1

    # return result

    # SC = O(1)
    j = 0
    for i in range(n):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1

    return arr



        

print(movezerostoend([5,0,5,0,3,4,0,2]))



        


