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

# =======================================================================================================
'''
    Modularizing code for reusability for different problems based on binary search
'''
class BinarySearch:
    def search(self, array, key, ascending = True):
        start = 0
        end = len(array) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if array[mid] == key:
                return mid
            elif key < array[mid]:
                if ascending:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if ascending:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1

    def firstOccuerence(self, array, key, first = True):
        # if first = True, i.e first occurence else last occurence 
        start = 0
        end = len(array) - 1
        firstIdx = -1
        lastIdx = -1
        while start <= end:
            mid = start + (end - start) // 2

            if array[mid] == key:
                if first:
                    firstIdx = mid
                    # once the key is found, we don't know whether it is first occuerence or not so
                    # move to the left side again
                    end = mid - 1
                else:
                    lastIdx = mid
                    # once the key is found, we don't know whether it is last occuerence or not so
                    # move to the right side again
                    start = mid + 1
            elif key < array[mid]:
                end = mid - 1
            else:
                start = mid + 1
        
        return firstIdx if first else lastIdx

    def countOfElement(self, array, key):
        # since the array is sorted, the repeated key will always be together, therefore the window length
        # of that repeated key = count of key.
        # e.g [1, 2, 2, 2, 5], count = indexOfLastOccurence - indexOfFirstOccurence + 1 -> (3 - 1) + 1 = 3

        firstIdx = self.firstOccuerence(array, key, first = True)
        lastIdx = self.firstOccuerence(array, key, first = False)

        if firstIdx == -1 and lastIdx == -1:
            return 0

        return (lastIdx - firstIdx) + 1


