# Time: O(n) and space: O(1)
def moveToEnd(array, target):
    i = 0
    j = len(array) - 1

    while i < j:
        # j should not get less than i
        while i < j and array[j] == target:
            j -= 1

        while i < j and array[i] != target:
            i += 1

        array[i], array[j] = array[j], array[i]

    return array

x = [3, 5, 2, 4, 1, 2, 3, 8, 2, 2, 2]

print(moveToEnd(x, 2))

        
        
