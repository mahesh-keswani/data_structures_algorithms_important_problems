class BST:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        currentNode = self

        while currentNode is not None:
            if value < currentNode.value:
                if currentNode.left is not None:
                    currentNode = currentNode.left
                else:
                    currentNode.left = BST(value)
                    break
            else:
                if currentNode.right is not None:
                    currentNode = currentNode.right
                else:
                    currentNode.right = BST(value)
                    break

    def search(self, value):
        currentNode = self

        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
            
        return False


    def invertTreee(self):
        if self is None:
            return
        
        self.left, self.right = self.right, self.left
        # if self.left exists
        if self.left:
            self.left.invertTreee()

        # if self.right exists
        if self.right:
            self.right.invertTreee()

    def recursivePreorder(self):
        if self is None:
            return
        print(self.value)

        # if self.left exists
        if self.left:
            self.left.recursivePreorder()

        # if self.right exists
        if self.right:
            self.right.recursivePreorder()
        
    
    def recursiveInorder(self):
        if self is None:
            return
        
        # if self.left exists
        if self.left:
            self.left.recursiveInorder()

        print(self.value)

        # if self.right exists
        if self.right:
            self.right.recursiveInorder()
           
    def recursivePostorder(self):
        if self is None:
            return
        
        # if self.left exists
        if self.left:
            self.left.recursivePostorder()

        # if self.right exists
        if self.right:
            self.right.recursivePostorder()

        print(self.value)

    def iterativeInorder(self):
        if self is None:
            return

        stack = []
        currentNode = self

        while len(stack) or currentNode:

            if currentNode is not None:
                stack.append(currentNode)
                currentNode = currentNode.left
            else:
                currentNode = stack.pop()
                print(currentNode.value)
                currentNode = currentNode.right

    def iterativePreorder(self):
        if self is None:
            return

        stack = []
        currentNode = self

        while len(stack) or currentNode:

            if currentNode is not None:
                print(currentNode.value)
                stack.append(currentNode)
                currentNode = currentNode.left
            else:
                currentNode = stack.pop()
                currentNode = currentNode.right
        
        
'''
    10
   /  \
  7     12
 / \   /  \
6   8 11   13
'''
root = BST(10)
root.insert(7)
root.insert(6)
root.insert(8)
root.insert(12)
root.insert(11)
root.insert(13)

print("Inorder")
root.recursiveInorder()

print("Preorder")
root.recursivePreorder()

print("Postorder")
root.recursivePostorder()

print( root.search(11) )

print(" Iterative Inorder ")
root.iterativeInorder()

print(" Iterative Preoder ")
root.iterativePreorder()
