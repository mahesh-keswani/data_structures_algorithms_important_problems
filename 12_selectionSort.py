# Time: O(n^2) and space: O(1)
def selectionSort(array):
    currentIndex = 0
    while currentIndex < len(array):
        smallestIdx = currentIndex

        for i in range(currentIndex + 1, len(array)):
            if array[i] < array[smallestIdx]:
                smallestIdx = i

        array[currentIndex], array[smallestIdx] = array[smallestIdx], array[currentIndex]
        currentIndex += 1

    return array

x = [5, 2, 4, 8, 1]
print(selectionSort(x))
