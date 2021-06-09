def swapSort(array):
    i = 0
    while i < len(array):
        # The correct position for the array[i] is array[i]-1, if array[i] is not at it's correct position
        # Then take it to it's correct position by swapping
        if array[i] != array[ array[i]-1 ]:
            array[i], array[ array[i]-1 ] = array[ array[i]-1 ], array[i]
        else:

            # Else if the array[i] is at it's correct position OR the element is duplicate, then just move forward.
            i += 1

    missing = []
    duplicates = []
    for i in range( len(array) ):
        if array[i] != (i + 1):
            missing.append( i + 1 )
            duplicates.append( array[i] )

    return missing, duplicates
