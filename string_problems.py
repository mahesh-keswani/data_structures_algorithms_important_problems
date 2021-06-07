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
    
