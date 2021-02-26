# Using Moore's voting algorithm
# Majority element is element, whose count > len(array) / 2
# idea is, keep track of count of current element, if (i + 1)th element is equal to ith element
# then increase the count, if not equal then decrease the count by 1, if count = 0, then keep track of current element
# count and set it's initial count to 1
# At the end, you will get some potential candidate for majority element
# Then again do one more iteration, and check if the count of element if > (n / 2), then it is result
# else there is no majority element

def majorityElement(array):
    count = 1
    potentialMajorityElement = array[0]

    for i in range(1, len(array)):
        if potentialMajorityElement == array[i]:
            count += 1
        else:
            count -= 1
            if count == 0:
                potentialMajorityElement = array[i]
                count = 1

    checkingCountOfPotentialElementIsMajority = 0
    for num in array:
        if num == potentialMajorityElement:
            checkingCountOfPotentialElementIsMajority += 1

    if checkingCountOfPotentialElementIsMajority > len(array) // 2:
        return potentialMajorityElement
    return -1

array = [8, 5, 8, 8, 2, 3, 5]
print( majorityElement( array ) )
