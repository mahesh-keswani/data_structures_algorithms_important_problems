# In this, we have to traverse through all the elements in the array, and each element represents the number of
# jumps, say arr[0]=2, then from 0th index we have to jump two positions and we will reach at index 2.
# we have to return true if we traversed all the elements and at the end we will reach the starting index
# if number of elements traversed < len(array) and we have reached the starting index then return false,
# also if there are multiple cycles then also return False.
# Also note that we have to traverse the array in the circular manner.

def singleCycleCheck(arr):
    numberOfElementsTraversed = 0
    STARTING_IDX = 0
    current_idx = STARTING_IDX

    while numberOfElementsTraversed < len(arr):
        # i.e we have reached a case where we reached at starting index without traversing all the elements.
        if (numberOfElementsTraversed > 0) and (current_idx == STARTING_IDX):
            return False

        numberOfElementsTraversed += 1
        current_idx = updateIdx(arr, current_idx)
    
    if numberOfElementsTraversed == len(array) and current_idx == STARTING_IDX:
        return True

    # ie we have reached the case where we have multiple cycles.
    return False

def updateIdx(arr, current_idx):
    # number of jumps we have to make
    jumps = arr[current_idx]

    # since we have to traverse in circular way
    current_idx = ( current_idx + jumps ) % len(arr)

    # absolute value because say, jumps = -26 and current_idx=0 and len(arr)=5
    # then current_idx = (0 + -26) % 5 -> -1
    return abs(current_idx)
