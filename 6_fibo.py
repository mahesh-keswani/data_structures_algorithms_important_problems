## Series: 0 1 1 2 3 5 8 ...

## Time: O(2^n) | space: O(n)
## space o(n) because at any point of time there are atmost n function calls in the stack.
def getNthFib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFib(n - 1) + getNthFib(n - 2)

## Time: O(n) | Space: O(n) (reason same as above)
def getNthFib(n, memoize = {1:0, 2:1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib(n - 1, memoize) + getNthFib(n - 2, memoize)
        return memoize[n]

# Time: O(n) and space: O(1)
def getNthFib(n):
    lastTwoFibs = [0, 1]
    current = 3

    while current <= n:
        nextFib = lastTwoFibs[0] + lastTwoFibs[1]
        lastTwoFibs[0] = lastTwoFibs[1]
        lastTwoFibs[1] = nextFib

##  there is special case when n = 1, it should return lastTwoFibs[0] instead of lastTwoFibs[1]    
    return lastTwoFibs[1] if n > 1 else lastTwoFibs[0]
