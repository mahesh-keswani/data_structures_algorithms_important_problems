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
