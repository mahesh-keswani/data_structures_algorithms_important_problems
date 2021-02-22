def checkSubsetWithSumK(array, k):
    n = len(array)
    dp = [ [False for sum in range(0, k + 1)] for size in range(0, n + 1)]

    # As subset with sum 0 is always possible ( always take null set )
    for i in range(0, n + 1):
        dp[i][0] = 1

    for row in range(1, n + 1):
        for col in range(1, k + 1):
            if array[row - 1] <= col:
                dp[row][col] = dp[row - 1][col - array[row - 1]] or dp[row - 1][col]
            else:
                dp[row][col] = dp[row - 1][col]

        
    return dp[-1][-1]

def countSubsetWithSumK(array, k):
    n = len(array)
    dp = [ [0 for sum in range(0, k + 1)] for size in range(0, n + 1)]

    for i in range(0, n + 1):
        dp[i][0] = 1

    for row in range(1, n + 1):
        for col in range(1, k + 1):
            if array[row - 1] <= col:
                dp[row][col] = dp[row - 1][col - array[row - 1]] + dp[row - 1][col]
            else:
                dp[row][col] = dp[row - 1][col]

        
    return dp[-1][-1]


# check if it is possible to divide the array into two subsets such that their sum is equal
def equalSumPartition(arr):
    '''
        let s1 = sum(subset1), s2 = sum(subset2), S = sum(whole array)
        As, s1 + s2 = S, we want s1 = s2, therefore, s1 + s1 = S, therefore S = 2s1,
        i.e if and only if S is even this task is possible, else not.
        Now idea is, if there exist one subset with sum S / 2, then other subset's sum will be automatically S - S/2
    '''
    sumOfArr = sum(arr)

    if sumOfArr % 2 != 0:
        return False
    half = sumOfArr // 2

    isSubsetWithSumHalfPresent = subsetWithSumK(arr, half)
    if isSubsetWithSumHalfPresent != 0:
        return True
    return False
