'''
    We are given the array which is supposed to be sorted, and it is almost sorted but some subarray
    of it is not sorted. We need to find the starting and ending indexes of that subarray.
'''

def subarraySort(array):

    # this is min element in unsorted subarray
    minElement = float("inf")

    # this is max element in unsorted subarray
    maxElement = float("-inf")
    
    for i in range(len(array)):
        num = array[i]

        if isOutOfOrder(num, i, array):
            minElement = min( minElement, num )
            maxElement = max( maxElement, num )

    # i.e all the elements were sorted
    if minElement == float("inf"):
        return [-1, -1]

    # try to find the correct position for minElement
    minElementIdx = 0
    while array[minElementIdx] <= minElement:
        minElementIdx += 1

    # try to find the correct position for maxElement
    maxElementIdx = len(array) - 1
    while array[maxElementIdx] >= maxElement:
        maxElementIdx -= 1

    return [minElementIdx, maxElementIdx]
        
def isOutOfOrder(num, i, array):
    if i == 0:
        # if ith element is > i+1, then it is out of order
        return array[i] > array[i + 1]

    if i == len(array) - 1:
        # if last element is < second last, then it is out of order
        return array[i] < array[i - 1]

    # if num is smaller than previous or it is greater than next, then it is out of order
    return num < array[i-1] or num > array[i+1]
