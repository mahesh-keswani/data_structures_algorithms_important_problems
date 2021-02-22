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
