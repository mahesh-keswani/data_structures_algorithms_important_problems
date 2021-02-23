def maxSumWithWindowK(arr, k):
    maxSoFar = sum(arr[:k])
    currentSum = maxSoFar
    # Try to run on simple example with window size atleast 3, code will make sense
    for i in range(k, len(arr)):
        currentSum = currentSum + arr[i] - arr[i - k]
        maxSoFar = max( maxSoFar, currentSum )
        
    return maxSoFar
