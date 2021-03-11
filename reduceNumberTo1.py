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
