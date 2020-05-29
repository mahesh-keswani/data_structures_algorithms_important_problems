# Time: O(n) and space: O(1)
def findLargestThree(array):
    largestThree = [None, None, None]
    for number in array:
        helperFunction(largestThree, number)

    return largestThree

def helperFunction(array, num):
    if array[2] is None or array[2] < num:
        shiftAndUpdate(array, num, 2)
    elif array[1] is None or array[1] < num:
        shiftAndUpdate(array, num, 1)
    elif array[0] is None or array[0] < num:
        shiftAndUpdate(array, num, 0)

def shiftAndUpdate(array, num, idx):
    for i in range(0, idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i + 1]

    return array

x = [10, 5, 7 , 9, 1]
print(findLargestThree(x))


