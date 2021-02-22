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

# Find the two subsets in an array, such that difference of their sums is minimum
def findTheTwoSubsetsWithMinDiff(arr):
    '''
        As s1 + s2 = S, s2 = S - s1, our initial objective is min s2 - s1, therefore objective becomes min (S - s1) - s1
        i.e min S - 2s1, minimum value of this obejctive is 0, when s1 = S/2
        Now range of values s1 can take is from 0 to S / 2, but some values will be possible (i.e True) and some
        will be not.
        e.g arr = [2, 7, 3], S = 12, therefore s1 can take from 0 to 6,
        sum 0, 2, 3, 5 these are the valid values of s1 (since subsets with this sum are present)
        sum 1, 4 is not possible
    '''
    sumOfArr = sum(arr)
    half = sumOfArr // 2
    n = len(arr)
    
    dp = [ [False for i in range(0, half + 1)] for j in range(0, n + 1)]
    for i in range(0, n + 1):
        dp[i][0] = True

    # If the element in the last row is True, that means this subset with sum=j is possible
    # i
    for i in range(1, n + 1):
        for j in range(1, half + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    minDiff = float("inf")
    for i in range(0, half + 1):
        if dp[-1][i]:
            minDiff = min( sumOfArr - 2*i, minDiff )
            print(minDiff)

    return minDiff
