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
