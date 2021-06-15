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

'''
    Since in this case, the array is infinite, we don't know the end of the array, so we start with start=0 and assume that end=1.
'''
def searchInInfiniteSortedArray(arr, x):
    start = 0
    end = 1
    
    # while the end element is less than the x, update the start=end and double the end.
    # e.g say arr=[1,2,3,4,....] say element to be searched is 5. initially start=0, end=1
    # since arr[end]<x, then we know the x will never be present before end index, i.e x=5 will never be present before index 1 as array is sorted.
    # therefore update the start=end first and then double the range for end.
    
    while arr[end] < x:
        start = end
        end = end * 2
    
    # after the above loop, the x will be bounded by the start and end, such that arr[start] < x < arr[end]
    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return -1


'''
    The array is unsorted, and we have to find the peek element. Peek element is basically element
    at index at index i which is greater than element at i-1 and also i+1. There can be multiple
    peek elements and you can return any of the peek element.
    Also for the elements at index 0 and index n-1, for index 0, it is also peek element if it is
    greater than element at index 1 (even though it does not have its i-1 element).
    Similarly for the element at n-1, if it is greater than n-2, then it is also peek element
    (even though it does not have right element)
'''

def peekElement(arr):
    start = 0
    end = len(arr) - 1
    n = len(arr)
    
    while start <= end:
        mid = start + (end - start) // 2

        if mid > 0 and mid < n-1:
            if (arr[mid] > arr[mid - 1]) and (arr[mid] > arr[mid + 1]):
                return mid

            if arr[mid - 1] > arr[mid]:
                end = mid - 1
            elif arr[mid + 1] > arr[mid]:
                start = mid + 1
        elif mid == 0:
            if arr[0] > a[1]:
                return 0
            else:
                return 1
        elif mid == n-1:
            if arr[n-1] > arr[n-2]:
                return n-1
            else:
                return n-2
            
    return -1
            
arr = [5, 10, 20, 15]
print( peekElement(arr) )

'''
    arr: each index i is one book and arr[i] represents number of pages in book.
    k: number of students

    we have to allocate books to student but with few restrictions:
    1) one student have to read the entire book, it is not allowed that one student reads
    half book and other student reads remaining half.
    2)Each student should have atleast one book.
    3) Books should be alloted in the contionous manner, e.g we have arr = [10, 20, 30, 40]
    and k=2, then student1 can get (10) and student2 can get (20, 30, 40) OR student1 (10, 20)
    and student2 (30, 40) OR student1 (10, 20, 30) and student2 (40).
    3) we have to minimize the maximum number of pages one student should read, e.g in the first
    case max number of pages one student can read is 90, in case2 it is 70 and in case3 it is 60.
    So we have to return 60.
'''

def isMidValid(arr, mid, k):
    pagesRead = 0
    students = 1 # this will keep count of number of students, initially we have one student only

    for pages in arr:
        pagesRead += pages

        # if at any time number of pages read > mid (max capacity for every student)
        if pagesRead > mid:
            # then we have introduce new student and set it's number of pages read=pages of current
            # book
            students += 1
            pagesRead = pages

        # if at any time number of students (having the capacity=mid) > then the given k
        # therefore this capacity is invalid, inorder to have only k students, we have to
        # increase the capacity, therefore start=mid+1 is there
        if students > k:
            return False

    # if we have not reached return False, then it means number of students=k, and therefore
    # the mid (capacity of student) is valid, therefore return True
    return True
        
def bookAllocation(arr, k):

    # if number of students given is greater than number of books, then we cannot allocate each student
    # one book, therefore return -1
    if k > len(arr):
        return -1
    
    # here range between start and end represents number of pages that student can read.

    # since each student should have atleast one book, therefore we start the range with book having
    # max number of pages
    start = max(arr)

    # maximum number of pages that one student can read is sum of all the pages given in array.
    end = sum(arr)

    result = float("inf")
    while start <= end:
        # this mid represents max number of student and we have to check if this mid is valid.
        mid = start + (end - start) // 2

        if isMidValid(arr, mid, k):
            result = min( result, mid )
            print(result)
            # now we know the current mid is valid, but we have to find minimum value for mid
            # in the range, so bring end=mid-1
            end = mid - 1
        else:
            # if the mid is invalid then
            start = mid + 1
            
    return result

def medianOfTwoSortedArrays(array1, array2, start_a, end_a, start_b, end_b):

    # when the number of elements in both the array are 2
    if (end_a - start_a == 1) and (end_b - start_b == 1):
        median = ( max( array1[start_a], array2[start_b] ) + min( array1[end_a] + array2[end_b] ) ) / 2
        return median
    
    # indices of the medians of two arrays
    m1 = (start_a + end_a) // 2
    m2 = (start_b + end_b) // 2

    # if the median of both the arrays are same, then the median of two sorted arrays will also be same
    if array1[m1] == array2[m2]:
        return array[m1]

    # if the median of array1 is less than median of array2
    # then, ignore the a1,a2...,m1 (first half of array1)
    # and ignore second half of array2
    elif array1[m1] < array2[m2]:
        start_a = m1
        end_b = m2
    else:
        # median of array2 < median of array1
        # then ignore first half of array2 and ignore second half of array1
        start_b = m2
        end_a = m1

    return medianOfTwoSortedArrays(array1, array2, start_a, end_a, start_b, end_b)
 
