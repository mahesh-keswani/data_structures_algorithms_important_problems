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


    def countSortedArrayIsRotated(self, array):
        '''
            when sorted array is rotated, then number of times it is rotated = indexOfMinElement.
            And min element is the only element in sorted rotated array, which is smaller than it's
            previous element as well as next element.
        '''
        lenArr = len(array)

        if lenArr == 0:
            return -1
        if lenArr == 1:
            return 0
        
        start = 0
        end = lenArr - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            # checking for the prev in circular way
            prev = (mid - 1 + lenArr) % lenArr
            # checking for next in circular way
            nextToMid = (mid + 1) % lenArr

            if array[mid] <= array[prev] and array[mid] <= array[nextToMid]:
                return mid
            # if mid > start, i.e left subarray is sorted, we need to go to right, where minimum will be present
            # in unsorted array 
            if array[mid] > array[start]:
                start = mid + 1
            # i.e right subarray is sorted we need to go to left
            elif array[mid] <= array[end]:
                end = mid - 1

        return -1

        
    def searchInRotatedSortedArray(self, array, key):
        minIdx = self.countSortedArrayIsRotated(array)

        # Now we know the index of minimum element, now as the key must be greater than min element
        # and as sorted array is rotated, we have to apply binary search on (start to minIdx) and (minIdx to end)
        # if both return -1, then key is not present in array, else return index of key
        left = self.search(array[ 0:minIdx ], key)
        # ... + minIdx because, consider this [7, 11, 12, 5, 6], minIdx = 3, then when we will do binary search
        # on [minIdx: len(array)], it will return 1, but in input array it's
        # index will be 3 (minIdx) + 1(search result of bs on [minIdx:end])
        
        right = self.search(array[ minIdx:len(array) ], key) + minIdx

        # instead of these 3 lines, we know one of them will be -1, therefore we can return max(left, right)
        # if both are -1, then -1 will be returned else index of key will be returned
        if left == -1 and right == -1:
            return -1
        
        return left if left != -1 else right

    def searchElementInNearlySortedArray(self, array, key):
        # nearly sorted array means, element at index i will be at index (i - 1) OR at i OR at (i + 1) in sorted array

        # handling edge cases in starting only
        if array[0] == key:
            return 0

        if array[-1] == key:
            return len(array) - 1

        start = 1
        end = len(array) - 2
        
        while start <= end:
            mid = start + (end - start) // 2

            if array[mid] == key:
                return mid
            elif mid > 0 and array[mid - 1] == key:
                return (mid - 1)
            elif mid < (len(array) - 1) and array[mid + 1] == key:
                return (mid + 1)
            # since now we have compared key with mid-1, now comparing with mid-2
            if key < array[mid - 2]:
                end = mid - 2
            elif key > array[mid + 2]:
                start = mid + 2
        return -1
    
    def findFloorAndCeil(self, array, key):
        # floor means, the closest element which is <= key
        # ceil means the closest element which is >= key
        # if parameter floor = False, then we will find ceil
        start = 0
        end = len(array) - 1
        floor = -1
        ceil = -1
        
        while start <= end:
            mid = start + (end - start) // 2
            # i.e if we have key present in the array then this is only floor and ceil
            if array[mid] == key:
                return mid
            # i.e for floor we want the key to be greater than array[mid] | array[mid], ..., key
            # for ceil, we want the key to be less than array[mid], key, ..., array[mid] (then only it will be potential ceil)
            elif key < array[mid]:
                ceil = mid
                end = mid - 1
            # i.e key > array[mid], i.e array[mid] < key then it is possible candidate for floor
            else:
                floor = mid
                start = mid + 1

        return floor, ceil
            
array = [7, 11, 12, 5, 6]
bs = BinarySearch()

# if array is right rotated 
print(len(array) - bs.countSortedArrayIsRotated(array))

# if array is left rotated 
print(bs.countSortedArrayIsRotated(array))

