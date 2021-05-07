'''
    say stack is [4, 1, 3, 2], first pop element and add it in helping stack. helpingStack = [2]
    Then new element will be 3, while the element in helpingStack is smaller than the popped element, pop the
    elements from the helpingStack and push it in stack.
    
'''

def sortStackUsingOneOtherStack(stack):
    helpingStack = [ stack.pop() ]
    
    while len(stack):
        temp = stack.pop()
        # while temp > top of helpingStack
        while len(helpingStack) and temp > helpingStack[-1]:
            # push the element back into stack 
            stack.append( helpingStack.pop() )

        helpingStack.append(temp)

    return helpingStack

stack = [4, 1, 3, 2]
print( sortStackUsingOneOtherStack(stack) )

'''
    Idea is, first we have to check if length is odd or even, then if length is odd, then move to next node.
    e.g 1 -> 2 -> 3 -> 2 -> 1,
    keep p and q to head, and move p by step and q by two steps, move till q.next is None or q is None,
    if q is None, then length is even, else if q.next is None then length is odd.
    First put elements in stack till middle - 1, skip middle, then pop one element from stack and compare with
    current node if equal then continue else return False.
             p    q
    1 -> 2 -> 2 -> 1
    stack = [1,2]
'''

def checkIfLinkedListIsPalindrome(head):
    p = head
    q = head
    stack = []
    while q is not None and q.next is not None:
        stack.append( p.value )
        
        p = p.next
        q = q.next.next
        
    # i.e length is odd
    if q and q.next is None:
        p = p.next

    while p is not None:
        nodeValue = p.value
        stackTop = stack.pop()

        if nodeValue != stackTop:
            return False

        p = p.next
        
    return True


'''
    Implement max stack: First way can be, if we implement stack using linked list, then in every node we will
    create three fields: value, oldMax, next
'''

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.oldMax = None

class MaxStack:

    def __init__(self):
        self.head = None
        self.max = None

    def push(self, x):
        newNode = Node(x)

        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
            
        if self.max is None or newNode.value > self.max:
            newNode.oldMax = self.max
            self.max = newNode.value

    def pop(self):
        if head is None:
            return None
        
        node = self.head
        self.head = self.head.next
        node.next = None
        # 2 -> 1
        # 1    N
        if node.value == self.max:
            self.max = node.oldMax

        return node.value

    def maxStack(self):
        return self.max

    def printStack(self):
        if self.head is None:
            return None

        node = self.head
        while node:
            print(node.value, node.oldMax)
            node = node.next
            
maxstack = MaxStack()
maxstack.push(3)
maxstack.push(7)
maxstack.push(4)
maxstack.push(5)

maxstack.printStack()

'''
    Another way of implementing max stack, Idea is, create a helperStack, pop top element from stack and
    insert into helperStack, now for every other element in stack, pop one element, compare with the top
    element of helperStack till it is smaller than top and push elements of helperStack again back to stack.

    helperStack will always keep track of max element.
'''

class Maxstack:

    def __init__(self):
        self.stack = []
        self.helperStack = []

    def push(self, x):
        self.stack.append(x)

        if len(self.helperStack) == 0:
            self.helperStack.append(x)
        else:
            # checking if top element of stack > top element of helperStack
            if self.stack[-1] > self.helperStack[-1]:
                self.helperStack.append( x )

        return self

    def pop(self):
        if len(stack) == 0:
            return None

        # if top of the stack == top of helper stack (max element), we should pop from helperStack also
        # as it's next top will be 2nd max
        if self.stack[-1] == self.helperStack[-1]:
            helperStackPop = self.helperStack.pop()

        stackPop = self.stack.pop()
        
        return stackPop

    def maxStack(self):
        if not len(self.stack):
            return None

        return self.helperStack[-1]

    def printStack(self):
        print(self.stack)
        print(self.helperStack)
        

stack = Maxstack()
stack.push(4).push(3).push(10).push(7)

stack.printStack()


'''
    Idea is: traverse frpm right, if stack is empty return -1, else if current element < stack_top return stack top,
    else, while the current element is greater than top, continously pop and push every element to stack after this.
    By using this stack approach, stack will contain only potential elements, so we don't need to parse through
    all n elements.
'''
def nearestGreaterElementToRight(array):
    # ngr -> nearest greater to right
    ngr = []
    stack = []
    for i in range(len(array) - 1, -1, -1):
        num = array[i]
        if len(stack) == 0:
            ngr.append(-1)
        # if num < stack top
        elif num < stack[-1]:
            ngr.append( stack[-1] )
        else:
            # while there is stack or num >= stack top
            while len(stack) > 0 and num >= stack[-1]:
                stack.pop()

            if len(stack) == 0:
                ngr.append(-1)
            else:
                # when this is reached, we are sure that stack top is > num
                ngr.append(stack[-1])

        stack.append( num )

    return list(reversed(ngr))

array = [2, 1, 4, 3, 6, 2]
print( nearestGreaterElementToRight(array) )

'''
    Same as nearest greater element to right, just traverse from left to right and there is no need to reverse
    the result
'''

def nearestGreaterElementToLeft(array):
    # ngr -> nearest greater to left
    ngl = []
    stack = []
    for i in range(0, len(array)):
        num = array[i]
        if len(stack) == 0:
            ngl.append(-1)
        # if num < stack top
        elif num < stack[-1]:
            ngl.append( stack[-1] )
        else:
            # while there is stack and num >= stack top
            while len(stack) > 0 and num >= stack[-1]:
                stack.pop()

            if len(stack) == 0:
                ngl.append(-1)
            else:
                # when this is reached, we are sure that stack top is > num
                ngl.append(stack[-1])

        stack.append( num )

    return ngl

array = [2, 1, 4, 3, 6, 2]
print( nearestGreaterElementToLeft(array) )

'''
    similar as nearest greater element to right, just convert all the greater than to less than and vice versa
'''

def nearestSmallerElementToRight(array):
    # nlr -> nearest smaller to right
    nlr = []
    stack = []
    for i in range(len(array) - 1, -1, -1):
        num = array[i]
        if len(stack) == 0:
            nlr.append(-1)
        # if num > stack top
        elif num > stack[-1]:
            nlr.append( stack[-1] )
        else:
            # while there is stack or num <= stack top
            while len(stack) > 0 and num <= stack[-1]:
                stack.pop()

            if len(stack) == 0:
                nlr.append(-1)
            else:
                # when this is reached, we are sure that stack top is > num
                nlr.append(stack[-1])

        stack.append( num )

    return list(reversed(nlr))

array = [2, 1, 4, 3, 6, 2]
print( nearestSmallerElementToRight(array) )

'''
    Same as nearest greater element to right, just traverse from left to right and there is no need to reverse
    the result and reverse the relational signs
'''

def nearestSmallerElementToLeft(array):
    # ngr -> nearest greater to left
    ngl = []
    stack = []
    for i in range(0, len(array)):
        num = array[i]
        if len(stack) == 0:
            ngl.append(-1)
        # if num > stack top
        elif num > stack[-1]:
            ngl.append( stack[-1] )
        else:
            # while there is stack and num <= stack top
            while len(stack) > 0 and num <= stack[-1]:
                stack.pop()

            if len(stack) == 0:
                ngl.append(-1)
            else:
                # when this is reached, we are sure that stack top is < num
                ngl.append(stack[-1])

        stack.append( num )

    return ngl

array = [2, 1, 4, 3, 6, 2]
print( nearestSmallerElementToLeft(array) )

'''
    Problem is: we have to find consecutive number of days the price was less than or equal to the ith day.
    Idea is: basically we have to find the nearest greater element to the left, but now instead of pushing
    just the element, we need to push the index as well, inorder to find the window size.
    Window size = i - index_of_nearest_greater_to_left
'''
def stockSpan(array):
    # ngr -> nearest greater to left
    ngl = []
    # [index, nearest_greater_to_left]
    stack = []
    for i in range(len(array)):
        num = array[i]
        if len(stack) == 0:
            ngl.append( -1 )
        # num  < stack top
        elif num < stack[-1][1]:
            ngl.append( stack[-1][0] )
        else:
            while len(stack) > 0 and num >= stack[-1][1]:
                stack.pop()

            if len(stack) == 0:
                ngl.append(-1)
            else:
                ngl.append( stack[-1][0] )

        stack.append( [i, num] )

    # now calculating window size
    spans = []
    for i in range(len(array)):
        spans.append( i - ngl[i] )

    return spans
        
array = [2, 1, 4, 3, 6, 2]
print( stockSpan(array) )

'''
    Idea is: find the nearest smaller to left (left), find nearest smaller to right (right), then find the width
    by right - left, and we already have the height of the rectansle, therefore we can get the area
'''

def nearestSmallerToLeft(array):
    nsl = []
    # again we are going to store the index as well
    # [index, nsl]
    stack = []
    for i in range(len(array)):
        num = array[i]
        if len(stack) == 0:
            nsl.append(-1)
        elif num > stack[-1][1]:
            nsl.append( stack[-1][0] )
        else:
            while len(stack) and num <= stack[-1][1]:
                stack.pop()

            if len(stack) == 0:
                nsl.append( -1 )
            else:
                nsl.append( stack[-1][0] )

        stack.append( [i, num] )

    return nsl

def nearestSmallerElementToRight(array):
    # nsr -> nearest smaller to right
    nsr = []
    stack = []
    for i in range(len(array) - 1, -1, -1):
        num = array[i]
        if len(stack) == 0:
            nsr.append(-1)
        # if num > stack top
        elif num > stack[-1][1]:
            nsr.append( stack[-1][0] )
        else:
            # while there is stack or num <= stack top
            while len(stack) > 0 and num <= stack[-1][1]:
                stack.pop()

            if len(stack) == 0:
                ngr.append( len(array) )
            else:
                # when this is reached, we are sure that stack top is > num
                nsr.append(stack[-1][0])

        stack.append( [i, num] )

    return list(reversed(nsr))

def maxAreaHistogram(array):
    nsl = nearestSmallerToLeft(array)
    nsr = nearestSmallerElementToRight(array)
    maxArea = float("-inf")
    
    for i, height in enumerate(array):
        width = nsr[i] - nsl[i] - 1
        currentArea = height * width
        maxArea = max( maxArea, currentArea )

    return maxArea

heights = [2, 1, 5, 6, 2, 3]
print( maxAreaHistogram(heights) )

'''
    In this, we will have binary matrix, we have to find all the possible rectangles and return the rectangle
    with max area.
    Idea is: It is similar to max area histogram, previously it was on 1D, now it is 2d, if we consider one row
    at a time, then it is 1d only.
    Consider below example, for first row max area = 2, now second row will be previous row + current_row,
    then finding max area on it, but we will add only if it is non zero.
    consider fourth row, till third row we will have [2, 3, 3, 3], for fourth row we will add only if it is non zero
    [3, 4, 0, 0]
'''
def maxAreaBinaryMatrix(matrix):
    # finding max area for first row
    currentRow = matrix[0]
    maxArea = maxAreaHistogram(currentRow)

    for i in range(1, len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                currentRow[j] = 0
            else:
                currentRow[j] = currentRow[j] + matrix[i][j]

        currentArea = maxAreaHistogram(currentRow)
        maxArea = max( currentArea, maxArea )

    return maxArea

matrix = [
    [0, 1, 1, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 0]
]

print( maxAreaBinaryMatrix(matrix) )

# For detailed explaination:
# https://www.youtube.com/watch?v=FbGG2qpNp4U&list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd&index=9
def rainWaterTrapping(arr):
    n = len(arr)

    # initializing with zero
    # mxl -> max element to the left, mxr -> max element to the right
    mxl = [0] * n
    mxr = [0] * n

    mxl[0] = arr[0]
    mxr[-1] = arr[-1]

    for i in range(1, n):
        mxl[i] = max(mxl[i-1], arr[i])

    for i in range(n-2, -1,-1):
        mxr[i] = max(mxr[i + 1], arr[i])

    area = 0
    for i, currHeight in enumerate(arr):
        width = 1
        height = min( mxr[i], mxl[i] ) - currHeight
        area += (width * height)

    return area



