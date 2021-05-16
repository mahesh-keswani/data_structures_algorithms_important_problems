def quickSort(array):
    quickSortHelper(array, 0, len(array) - 1)
    return array

def quickSortHelper(array, start, end):
    if start > end:
        return

    pivotIdx = start
    leftIdx = pivotIdx + 1
    rightIdx = end

    while leftIdx <= rightIdx:
        if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
            swap(leftIdx, rightIdx, array)

        if array[leftIdx] <= array[pivotIdx]:
            leftIdx += 1

        if array[rightIdx] >= array[pivotIdx]:
            right -= 1

    swap(pivotIdx, rightIdx, array)

    # now calling quicksort first on the subarray  which is smaller (if left subarray is smaller then call on left first)
    # then on right subarray

    # lenght of left subarray
    leftLenght = (right - 1) - start

    # length of right subarray
    rightLenght = end - (right + 1)

    if leftLenght <= rightLenght:
        quickSortHelper(array, start, rightIdx - 1)
        quickSortHelper(array, rightIdx + 1, end)
    else:
        quickSortHelper(array, rightIdx + 1, end)
        quickSortHelper(array, start, rightIdx - 1)

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
