# Time: O(n^2) | Space: O(1)
def bubbleSort(array):
    isSorted = False
    
    while not isSorted:
        isSorted = True
        
        for i in range(0, len(array) - 1):
            if array[i] > array[i + 1]:
               array[i], array[i + 1] = array[i + 1], array[i]
               isSorted = False

        if isSorted:
            break

    return array

x = [10, 5, 11, 6, 8]
print(bubbleSort(x))
            
