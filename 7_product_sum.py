# Time: O(N), here N is number of elements in array + number of element in every inner array
# in this example: N = 6(6 elements of 1st dimension) + 3(3 elements of inner array) = 9

# Space: O(d), here d is the depth of the array, in this example depth = 2
def productSum(array, multiplier = 1):
    result = 0
    for element in array:
        if type(element) is list:
            result += productSum(element, multiplier + 1)
        else:
            result += element

    return result * multiplier

x = [5, -2, 8, [4, 6, -3], 2, 1]

print(productSum(x))
