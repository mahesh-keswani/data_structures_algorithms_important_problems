# Sort the array in such a way that, all the elements which are not multiple of x should not change their positions, but the multiple of x should be in sorted order
# e.g array = [15, 2, 20, 5, 7], x = 5
# output: array = [5, 2, 15, 20, 7] all the non multiples of x stay at their positions and all multiples of 5 are in sorted order

def sort(array, x):
    multipleOfX = []
    for num in array:
        if num % x == 0:
            multipleOfX.append(num)

    multipleOfX.sort()

    j = 0
    for i in range(len(array)):
        if array[i] % x == 0:
            array[i] = multipleOfX[j]
            j += 1

    return array
