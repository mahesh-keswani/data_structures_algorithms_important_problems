# Time: O(n^2) because we are iterating through a string and concatinating with new string, which is not a constant
#       operation, time for concatination = (length of newString) + (len of string to be appended)
# Space: O(n) for storing the reversed string
def isPalindrome(string):
    newString = ""
##  reversing the string
    for i in reversed(range(len(string))):
        newString += string[i]

    return newString == string


# Time: O(n) for iteration, appending is constant time operation
# Space: O(n) same as above
def isPalindrome(string):
    newString = []
##  reversing the string
    for i in reversed(range(len(string))):
        newString.append(string[i])

    return "".join(newString) == string

# Time O(n) because slicing is O(k) operation where k is length of the slice
# Space: O(1)
def isPalindrome(string):
    return string == string[::-1]
