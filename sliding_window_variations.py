from collections import deque

def maxSumWithWindowK(arr, k):
    maxSoFar = sum(arr[:k])
    currentSum = maxSoFar
    # Try to run on simple example with window size atleast 3, code will make sense
    for i in range(k, len(arr)):
        currentSum = currentSum + arr[i] - arr[i - k]
        maxSoFar = max( maxSoFar, currentSum )
        
    return maxSoFar

'''
    Easier as compared to the previous approach.
'''
def maxInK(array, k):
    # assuming the first element as maximum element
    maxEle = array[0]
    queue = [0]
    # traversing through first k elements
    for i in range(1, k):
        
        # if we have found the element which is greater than maxEle than all the previous elements are basically useless so pop them out
        # e.g consider [1, 3, 2, 4] and k = 3, here maxEle initially = 1, then from 1..k, 3 will be maxEle i.e that previous element will
        # never going to be a part of maximum for the current window so remove it. 
        if array[i] > maxEle:
            maxEle = array[i]
    
            while queue and queue[0] < i:
                queue.pop(0)
        
        # if the element is not the maxEle, but it can be potential candidate when the window slides, so append it in the queue.
        queue.append(i)
    
    # here i will be the ending of sliding window and (i - k) will be starting of the window
    for i in range(k, len(array)):
        
        # if we have max ele in the window, then print it.
        if queue:
            print( array[queue[0]], end = ' ' )
        
        # removing all the elements which are invalid, i.e having index <= starting index of current window
        while queue and queue[0] <= (i - k):
            queue.pop(0)
        
        # again same logic, if currentEle > maxEle, remove all the elements which are not going to be required.
        if array[i] > maxEle:
            maxEle = array[i]

            while queue and queue[0] < i:
                queue.pop(0)

        queue.append(i)
        
    # for the last window the value will not going to be printed, so printing the maximum element for the last window
    if queue:
        print( array[queue[0]], end = ' ' )
        
def findLargestSubarrayWithSumK(arr, k):
    i = 0
    j = 1
    curSum = arr[i] + arr[j]
    maxWindowSize = -float("inf")
    # arr = [2, 1, 3, 4, 0, 1]
    # 
    while j < len(arr):
        print(curSum, maxWindowSize)
        if curSum < k:
            j += 1
            if j == len(arr):
                break
            curSum += arr[j]
        elif curSum > k:
            curSum -= arr[i]
            i += 1
        else:
            maxWindowSize = max(maxWindowSize, j - i + 1)

            # Now moving forward, looking for larger window size
            j += 1
            if j == len(arr):
                break
            curSum += arr[j]

    return maxWindowSize

def longestStringWithKUniqueChars(string, k):
    charCount = {}
    i = 0
    j = 0

    maxLenght = -float("inf") 
    # aacbbb
    # 
    while j < len(string):
        currentChar = string[j]

        if string[j] not in charCount:
            charCount[ string[j] ] = 1
        else:
            charCount[ string[j] ] += 1
                
        if len(charCount) > k:
            while len(charCount) != k:
                charCount[ string[i] ] -= 1

                if charCount[ string[i] ] == 0:
                    del charCount[ string[i] ]
                else:
                     i += 1
                                 
        maxLenght = max(maxLenght, j - i)
            
        j += 1
        
    return maxLenght

def longestSubstringAllUniqueChars(string):
    charCount = {a:1, b:1, c:1}
    i, j = 0, 0
    maxLength = -float("inf")
    # abcad
    while j < len(string):
        currentChar = string[j]

        if currentChar not in charCount:
            charCount[ currentChar ] = 1
        else:
            charCount[ currentChar ] += 1

        # at every time check, if len of dictionary is less than window size, then character has occured which is repeated
        # in substring, so we have to start decreasing window until it is equal = len(dictionary)
        # i.e all the characters in window size are unique
        if len(charCount) < (j - i + 1):
            while len(charCount) != (j - i + 1):
                charCount[ string[i] ] -= 0

                if charCount[ string[i] ] == 0:
                    del charCount[ string[i] ]
                i += 1
                
        maxLength = max( maxLength, j - i )

        j += 1

    return maxLength






















