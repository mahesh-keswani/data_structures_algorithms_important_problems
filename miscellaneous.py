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
