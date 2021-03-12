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
