# Time: O(nlog(n) + mlog(m)), time for sorting first and second array
#       Time for iteration ( which is O(max(n, m)) ) is dominated by time for sorting
# Space: O(1)
def smallestDiff(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    i = 0
    j = 0
    smallest = float("inf")
    current = 0
    pairs = []

    while i < len(arrayOne) and j < len(arrayTwo):
        firstNum = arrayOne[i]
        secondNum = arrayTwo[j]

        if firstNum < secondNum:
            current = secondNum - firstNum
            i += 1
        elif firstNum > secondNum:
            current = firstNum - secondNum
            j += 1
        else:
            return [firstNum, secondNum]

        if smallest > current:
            smallest = current
            pairs = [firstNum, secondNum]

    return pairs


x = [8, 14, 19, 36, 9]
y = [81, 27, 33, 43, 11]

print(smallestDiff(x, y))
