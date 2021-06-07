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


