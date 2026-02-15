def kadane(arr):
    n = len(arr)
    res = []
    currentsum = 0
    maxi = 0
    for i in range(n):

        currentsum += arr[i]

        if currentsum > 0:
            
            maxi = max(maxi, currentsum)
            res.append(arr[i])

        else:
            currentsum = 0
            res.clear()

    return res

print(kadane([2,-6,4,-10,6,3,7]))