'''
    In quickSelect, we have to find kth smallest (or largest) element in array. Idea is, say we want 2nd smallest element
    and after one iteration of quicksort, say the pivotIdx is 4, then we know the 2nd smallest element will be index
    1, so we apply quicksort iteratively till we reach the required position (k - 1 index) 
'''

def quickSelect(array, k):
    start = 0
    end = len(array) - 1
    position = k - 1

    while start <= end:
        pivotIdx = start
        left = pivotIdx + 1
        right = end

        while left <= right:
            if (array[left] > array[pivotIdx]) and (array[right] < array[pivotIdx]):
                swap(left, right, array)

            if array[left] <= array[pivotIdx]:
                left += 1

            if array[right] >= array[pivotIdx]:
                right -= 1

        swap(pivotIdx, right, array)

        if pivotIdx == position:
            return array[pivotIdx]

        # i.e pivot is on the left side of position, so start applying quicksort on the right side. 
        if pivotIdx < position:
            start = pivotIdx + 1
        elif pivotIdx > position:
            # i.e pivot is on the right of the position, so move to the left
            end = pivotIdx - 1

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
