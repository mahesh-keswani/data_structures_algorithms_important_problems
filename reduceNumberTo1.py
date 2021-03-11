'''
    Given a number n, we have to reduce it to 1 in min number of steps, by following one of the operations from below:
    1) if n is even, divide it by 2
    2) if n is odd, then you can add +1 to it or -1 to it, at the end it should be reduced to 1 in min steps
'''
def reduceNumberTo1Naive(n):
    if n == 1:
        return 0
    
    if n % 2 == 0:
        # if even, 1 for one step
        return 1 + reduceNumberTo1Naive(n // 2)
    # else count the number of steps for both n-1
    return 1 + min( reduceNumberTo1Naive(n - 1), reduceNumberTo1Naive(n + 1) )

'''
    Better way is, if n is even then divide it by 2, if n is odd, then when it is divided by 4 the possible remainder
    can be 1 or 3, if remainder is 3, then it will make sense to add 1 to it (e.g if n = 19, n % 4 == 3),
    by adding one it will be even and converge to 1 faster.
    if remainder is 1, then it will converge to 1 faster when it is subtracted 1 from it. 
'''

def reduceNumberto1Optimal(n):
    count = 0

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            # n == 3(special edge case), by this edge case it will be minimum else it will take one extra step 
            # decrement by 1
            if n % 4 == 1 or n == 3:
                n -= 1

            if n % 4 == 3:
                n += 1
        count += 1

    return count

n = 13
print( reduceNumberTo1Naive(n) )
print( reduceNumberto1Optimal(n) )
