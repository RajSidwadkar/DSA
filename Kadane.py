arr = [-1, 5, -6, 3, 3, -4, 5, 5]

def Kadane(arr):
    currentsum = 0
    maxsum = float('-inf')

    for i in range(len(arr)):
        currentsum += arr[i]
        maxsum = max(maxsum, currentsum)
        if currentsum< 0:
            currentsum = 0
            
    return maxsum

print(Kadane(arr))
            