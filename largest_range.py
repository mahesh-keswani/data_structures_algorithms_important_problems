# problem is, we have to find the largest range which is present in the given array, and note that the range need not
# to be continous
# So idea is, we will traverse the array and for each element we will move to its left and check if that exists
# in array and similarly we will also move right. Along with the we will keep track of visited elements

def largestRange(array):
    longestRange = 0
    bestRange = []

    # adding all the elements in visited and setting its value to False
    visited = {}
    for num in array:
        visited[num] = False

    
    for i in range(array):
        num = array[i]
        if visited[ num ]:
            continue

        # if not visited
        left = num - 1
        right = num + 1
        currentRangeLenght = 1

        # while the element exist in the array, going to the left for each element
        while left in visited:
            currentRangeLenght += 1
            visited[left] = True
            left -= 1

        # going to the right for each element
        while right in visited:
            currentRangeLenght += 1
            visited[right] = True
            right += 1

        if currentRangeLenght > longestRange:
            longestRange = currentRangeLenght
            bestRange = [left + 1, right - 1]

    return bestRange
