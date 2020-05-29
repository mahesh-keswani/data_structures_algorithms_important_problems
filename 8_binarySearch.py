# Time: O(log(n)) and space: O(log(n))
def binarySearch(array, target):
    binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2
    if target == array[middle]:
        return middle
    elif target < array[middle]:
        return binarySearchHelper(array, target, left, middle - 1)
    else:
        return binarySearchHelper(array, target, middle + 1, right)

# Iterative way
# Time: O(log(n)) and space: O(1)
def binarySearch(array, target):
    binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(array, target, left, right):
    while left < right:
        middle = (left + right) // 2

        if target == array[middle]:
            return middle
        elif target < array[middle]:
            right = middle - 1
        else:
            left = middle + 1

    return -1
