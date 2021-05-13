def kadaneAlgo(arr):
    maxEndingHere = arr[0]
    maxSoFar = arr[0]
    start = 0
    end = 0
    
    for i in range(1, len(arr)):
        num = arr[i]
        currentSum = maxEndingHere + num
        
        if num > currentSum:
            start = i
        maxEndingHere = max(currentSum, num)

        maxSoFar = max(maxEndingHere, maxSoFar)
        if maxSoFar > maxEndingHere:
            end = i
            
    return maxSoFar, [start, end]
