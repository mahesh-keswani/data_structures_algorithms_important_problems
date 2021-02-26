from collections import deque

def maxSumWithWindowK(arr, k):
    maxSoFar = sum(arr[:k])
    currentSum = maxSoFar
    # Try to run on simple example with window size atleast 3, code will make sense
    for i in range(k, len(arr)):
        currentSum = currentSum + arr[i] - arr[i - k]
        maxSoFar = max( maxSoFar, currentSum )
        
    return maxSoFar


def findMaxInEveryWindow(arr, k):
    '''
        Create a dequeue to store element indices.
        Iterate through the array, insert the indices of first K elements in the array
        (indices will be stored according to decreasing order of elements) .
        While insertion we will take care of the window such that there are no unnecessary indices (out of window elements).
        To remove these indices, we will remove all the elements from the back of the queue that is smaller
        than the current array element.
        After the iteration for the first K element, the maximum element's index is at the front of the queue.
        Now, Iterate through the remaining part of the array and remove the element from the front if they are out of the current window.
        Again, insert the element in the dequeue and before inserting delete those unnecessary indices which are smaller than the current array element.
    '''
    # [2, 1, 3, 4, 3, 5]
    # [3, ]
    myDeque = deque()
    for i in range(k):
        # checking if there is atleast one element and the current element is greater than the element at the end of queue
        # if so pop the element from rear
        while myDeque and arr[i] >= arr[ myDeque[-1] ]:
            myDeque.pop()

        # inserting the index at the rear end
        myDeque.append(i)

    for i in range(k, len(arr)):
        # As the front of queue contains max element of first window print it
        print(arr[ myDeque[0] ], end = " ")
        
        # cheking if there are any elements in deque and if there are any elements which are out of
        # current window, if yes Remove the elements from left
        while myDeque and myDeque[0] <= i - k:
            myDeque.popleft()

        # Remove all elements smaller than
        # the currently being added element 
        # (Remove useless elements)
        while myDeque and arr[i] >= arr[ myDeque[-1] ] :
            myDeque.pop()

        # Add current element at the rear of Qi
        myDeque.append(i)

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






















