# reference: https://www.geeksforgeeks.org/multiply-large-numbers-represented-as-strings/
def multiplyLargeNumbers(s1, s2):
    n1 = len(s1)
    n2 = len(s2)

    # to store the result in the reverse order
    result = [0] * (n1+n2)

    iForS1 = 0

    # traverse the s1, s2 backwards
    for i in range(n1-1, -1, -1):
        carry = 0
        iForS2 = 0

        for j in range(n2-1, -1, -1):

            # Multiply with current digit of first number 
            # and add result to previously stored result
            # at current position.
            currentSum = int(s1[i]) * int(s2[j]) + result[iForS1 + iForS2] + carry

            # Carry for next iteration
            carry = currentSum // 10

            # store the result
            result[iForS1 + iForS2] = currentSum % 10

            iForS2 += 1

        # at the end, if carry is generated, then store it in result
        if carry > 0:
            result[iForS1 + iForS2] += carry

        iForS1 += 1
        
    # print the result
    for digit in reversed(result):
        print(digit, end = '')

        
'''
    We can break this problem of fourNumberSum (x + y) + (z + k) = targetSum into two-sum problem.
    Say P = (x + y) and Q = (z + k), then we just have to find all (P + Q) which can sum to targetSum.
    But we have to make sure that we don't include same quadruplets multiple times with different order.
    For this, Idea is, for every index in array, first we will go to its right and calculate P and Q,
    if we found a targetSum, the for every pair which generated Q, we will form the quadruplets.
'''

def fourNumberSum(array, targetSum):
    allPairSums = {}
    result = []

    for i in range(1, len(array)):
        
        for j in range(i+1, len(array)):
            P = array[i] + array[j]
            Q = targetSum - P

            if Q in allPairSums:
                # a single sum can be found by multiple pairs in the array.
                # say array = [1, 3, -1, 4, 0] and say Q=4, then in dictionary
                # dictionary[4] = [ [1,3], [4,0] ]
                for pair in allPairSums[Q]:
                    result.append( pair + [P, Q] )

        for k in range(0, i):
            P = array[i] + array[k]

            if P not in allPairSums:
                allPairSum[P] = [ [array[i], array[k]] ]
            else:
                allPairSums[P].append( [array[i], array[k]] )

    return result

'''
    Idea is, remove one element from array and store remaining elements in new array (we don't modify
    the original array), and the removed element in the current permutation. We will remove element
    every time from new array, and when finally the new array will be empty, that is one permutation
    is formed, so store it in the final permutations list.
'''

def getPermutations(array):
    permutations = []
    permutationsHelper( array, [], permutations )
    return permutations

def permutationsHelper( array, currentPermutations, permutations ):

    # if the currentArray is empty and we have elements in the currenPermutation, then store it
    # permutations. The second check was necessary because, if the input to the program is empty array
    # then we would have stored in permutations = [ [] ], we don't want to do that.
    if len(array) == 0 and len(currentPermutations):
        permutations.append( currentPermutation )

    for i in range(0, len(array) -1):
        # removing the ith element, and storing the remaining elements in newArray
        newArray = array[:i] + array[i+1:]

        # creating the newPermutation list because, if we modify the same currentPermutation, then
        # things will not go as thought of.
        newPermutation = currentPermutation + [ array[i] ]

        # passing the newArray, newPermutations and final list of permutations
        permutationsHelper( newArray, newPermutation, permutations )

def combinationSums(array, target):
    result = set()
    findCombinations( array, target, 0, [], result )
    return result

def findCombinations(array, target, index, current, result):
    # i.e if the elements of the currentCombinations sums to target
    # since we cannot add the list to the set, therefore first convert it to tuple.
    if target == 0:
        result.add( tuple(current[:] )) 
        return

    # if the elements in the currentcombinations sums greater than target
    if target < 0:
        return

    for i in range(index, len(array)):
        # first add the element in the combination and check if we can add more elements which sums
        # to target-element, we simulated the adding of element in the current combination
        current.append( array[i] )
        findCombinations( array, target - array[i], i+1, current, result )

        # now remove the last element added and try again for other combination
        current.pop( len(current) - 1 )

array = [ 1, 1, 2, 7, 6 ]
target = 8

print( combinationSums(array, target) )

def zigzagTraverse(matrix):
    height = len(matrix) - 1
    width = len(matrix[0]) - 1

    row, col = 0, 0
    goingDown = True
    result = []

    while isValidPosition(row, col, width, height):
        result.append( matrix[row][col] )
        
        if goingDown:
            if col == 0 or row == height:
                goingDown = False
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if row == 0 or col == width:
                goingDown = True
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1

    return result

def isValidPosition(row, col, width, height):
    return 0 <= row <= height and 0 <= col <= width 


'''
    Reference: https://www.geeksforgeeks.org/convert-number-to-words/
'''

def convertNumberToWords(n):
    if n < 0:
        return "Minus {}".format(-n)

    ones = ["zero", "one", "two",   "three", "four", "five", "six", "seven", "eight", "nine",
            "ten",      "eleven",  "twelve", "thirteen",  "fourteen", "fifteen", "sixteen",
            "seventeen", "eighteen", "nineteen"]

    tens = ["", "",  "twenty", "thirty", "forty",   "fifty",
            "sixty",  "seventy", "eighty", "ninety" ]

    if n < 20:
        return ones[n]

    if n < 100:
        string = tens[ n // 10 ] + " " + ones[ n % 10 ]
        return string

    if n < 1000:
        string = ones[ n // 100 ] + " hundred and " + convertNumberToWords(n % 100)
        return string

    if n < 10000:
        string = ones[ n // 1000 ] + " thousand " + convertNumberToWords(n % 1000)
        return string

    '''
        And we can continue for larger numbers
    '''

'''
    We have to do (a*b) % n, but direct a*b can cause overflow, so Idea is, represent this in
    different way: (a*b) = (2*a) * (b/2), if b is even
                         = a + a*(b-1), if b is odd

    One Formula for (a*b) % n = ( (a%n) * (b%n) ) % n, but for large numbers of (a%n) and
    (b%n), multiplication can cause overflow, therefore use above method.
'''

def abModn(a, b, n):
    a = a % n
    result = 0
    
    while b > 0:
        # if b is odd, a will get added only for the odd b
        if (b & 1):
            result = ( result + a ) % n

        # if b is even 
        a = (2 * a) % n

        # right shift b by 1, i.e b = b // 2
        b = b >> 1

    return result % n
