# idea is, we will sort each string in list of strings and store in mapping as a key, it's value will
# be list having it's anagrams

def groupAnagrams(strings):
    mapping = {}

    for string in strings:
        stringSorted = "".join(sorted(string))

        if stringSorted in mapping:
            mapping[stringSorted].append(string)
        else:
            mapping[stringSorted] = [string]

    for key in mapping:
        print(key, "\t", mapping[key])

'''
    Idea is, we will consider each character in string as center of potential palindrome. The palindrome  can be
    even length or odd length, therefore for each character we will take it as center for even as well as odd, and
    keep track of maximum length of palindromic substring. 
'''
def longestPalindromicSubstring(string):
    # this contains the start and end of longest palindromic substring.
    # [0, 1] because at the end we will do slicing, we will return string[ longestPal[0]:longestPal[1] ]
    
    longestPal = [0, 1]
    for i in range(1, len(string)):
        # considering i as the center for odd palindrome.
        odd = getLongestPalindrome( string, i-1, i+1 )

        # considering center between i-1 and i of even length palindrome
        even = getLongestPalindrome( string, i-1, i )

        # the format of odd and even will be same as longestPal
        longest = max( odd, even, key = lambda x: x[1] - x[0] )

        longestPal = max( longestPal, longest, key = lambda x: x[1] - x[0] )

    return string[ longestPal[0]:longestPal[1] ]

def getLongestPalindrome(string, left, right):
    
    while left >= 0 and right < len(string):
        if string[left] != string[right]:
            break

        left -= 1
        right += 1

    return [ left + 1, right ]
    
'''
    Idea is, we will create a boolean 2d matrix for all the possible substrings whether they are palindrome
    or not. This 2d matrix will help in calculating min cuts at every position. 
'''
def isPalindrome(string, i, j):
    while i <= j:
        if string[i] != string[j]:
            return False

        i += 1
        j -= 1

    return True

def minCutsPartitioningToMakePalindrome(string):
    palindromes = [ [False for i in string] for j in string]
    n = len(string)
    for i in range(n):
        for j in range(i, n):
            palindromes[i][j] = isPalindrome(string, i, j)

    # placeholder for min cuts at every position
    cuts = [float("inf") for i in string]
    cuts[0] = 0
    for i in range(1, n):

        # checking if the string is palindrome
        if palindromes[0][i]:
            cuts[i] = 0
        else:
            # if not palindrome, then temporarily set, min number of cuts at previous position + 1
            cuts[i] = cuts[i - 1] + 1

        # now iterate from 1..i and check if any palindrome exits in between, if yes then update cuts
        for j in range(1, i):
            if palindromes[j][i] and (cuts[j] + 1 < cuts[i]):
                cuts[i] = cuts[j] + 1

    return cuts[-1]


'''
    Idea is, we will again create the 2d boolean matrix for all substrings whether they are palindrome or not.
    But this time we will not call isPalindrome for every substring, instead, check if first and last character
    are equal, if yes, then check if middle substring is palindrome, which is already solved.
'''

def minCutsPartitioningToMakePalindrome(string):
    palindromes = [ [False for i in string] for j in string]
    n = len(string)

    # setting palidrome=True for every single character in string 
    for i in range(n):
        palindromes[i][i] = True

    # Now we are done with palindromes of length 1, now lets check for length 2...n (n inclusive)
    # because it is possible that the entire string is palindrome.
    
    for length in range(2, n + 1):
        for startIdx in range(0, n - length + 1):
            # say n=10 and length=2, then we will find all the substrings of length 2 if we iterate from 0 till (10-2)
            # i.e (n-length)
            
            endIdx = startIdx + length - 1

            # if length==2, then we just have to check if startChar == endChar, elif length > 2, then
            # check startChar == endChar and middle substring is palindrome

            if length == 2:
                palindromes[startIdx][endIdx] = string[startIdx] == string[endIdx]
            else:
                result = (string[startIdx] == string[endIdx]) and palindromes[startIdx + 1][endIdx - 1]

    # placeholder for min cuts at every position
    cuts = [float("inf") for i in string]
    cuts[0] = 0
    for i in range(1, n):

        # checking if the string is palindrome
        if palindromes[0][i]:
            cuts[i] = 0
        else:
            # if not palindrome, then temporarily set, min number of cuts at previous position + 1
            cuts[i] = cuts[i - 1] + 1

        # now iterate from 1..i and check if any palindrome exits in between, if yes then update cuts
        for j in range(1, i):
            if palindromes[j][i] and (cuts[j] + 1 < cuts[i]):
                cuts[i] = cuts[j] + 1

    return cuts[-1]

'''
    Idea is, we will keep two pointers, one at the end of s1 and one at end of s2. if the character
    is matched, then decrement both the pointers, else decrement first pointer.
    If at the end, second pointer is -1, i.e we have found s2 in s1, else not found
'''
def checkIfOneStringIsSubsetOfOther(s1, s2):
    i = len(s1) - 1
    j = len(s2) - 1

    # i.e length of s1 is smaller than length of s2, then s2 cannot be subset of s1
    if i < j:
        return False
        
    while i >= 0 and j >= 0:
        s1Char = s1[i]
        s2Char = s2[j]

        if s1Char == s2Char:
            i -= 1
            j -= 1
        else:
            i -= 1

    # if j == -1 at the end, i.e all characters of s2 found in s1, else s2 is not subset of s1
    return j == -1


def generateAllSubsetsHelper(string, current, allCombinations):
    if len(string) == 0:
        allCombinations.append( current )
        return

    # add the first character of the string to the newCurrent
    newCurrent = current + string[0]

    # newString becomes
    reducedString = string[1:]

    # include the first character into the current
    generateAllSubsetsHelper(reducedString, newCurrent, allCombinations)

    # don't include the first character into the current
    generateAllSubsetsHelper(reducedString, current, allCombinations)

def generateAllSubsets(string):
    allCombinations = []
    generateAllSubsetsHelper(string, '', allCombinations)
    return allCombinations


'''
    Idea is, we will traverse both the strings from right to left, and sum them, if carry is generated
    then pass it to the next iteration.
'''
def addStrings(s1, s2):
    i = len(s1) - 1
    j = len(s2) - 1

    carry = 0
    result = ''
    while i >= 0 or j >= 0:
        # curSum = carry + s1[i] + s2[j]
        curSum = carry

        if i >= 0:
            curSum += ( ord( s1[i] ) - ord('0') )
            i -= 1

        if j >= 0:
            curSum += ( ord(s2[j]) - ord('0') )
            j -= 1

        # update the carry
        carry = curSum // 10

        # get the digit
        curSum = curSum % 10

        # append it to the result
        result += str(curSum)

    # if at the end carry is > 0
    if carry:
        result += str(carry)

    return result[::-1]
