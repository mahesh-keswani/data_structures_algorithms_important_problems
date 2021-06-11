# Right threaded binary tree
class ThreadedBinaryTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.isThread = False

    def insert(self, value):
        newNode = ThreadedBinaryTree(value)
        
        if self is None:
            self = newNode
            return self
        
        parent = None
        current = self

        # keep track of the parent node while finding correct position for new node
        while current:
            parent = current
            if value < current.value:
                current = current.left
            else:

                # the isThread will be True only if leaf is reached
                if current.isThread:
                    # set the current to None to exit the loop
                    current = None
                else:
                    current = current.right

        # checking if the newNode should be the left child of parent
        if newNode.value < parent.value:
            # Point the thread to the parent
            newNode.right = parent
            newNode.isThread = True

            parent.left = newNode
        else:
            # newNode is right child of parent

            # set the right thread to point to parent's right
            newNode.right = parent.right
            newNode.isThread = True

            # now set the parent isThread to False
            parent.right = newNode
            parent.isThread = False
  
        return self
    
    def search(self, value):
        current = self
        while current:
            if current.value == value:
                return True

            if value < current.value:
                current = current.left
            else:
                # i.e we have reached the leaf node
                if current.isThread:
                    break
                else:
                    current = current.right

        return False
