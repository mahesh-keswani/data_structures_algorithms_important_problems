# Reference: https://www.geeksforgeeks.org/avl-tree-set-1-insertion/

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVL:

    def insert(self, root, value):
        # First perform the standard bst insertion
        
        # crossed the leaf node
        if root is None:
            return Node(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert( root.right, value )

        # update the height of the root.
        root.height = 1 + max( self.getHeight(root.left), self.getHeight(root.right) )
        balance = self.balanceFactor(root)

        # left-left case
        if balance > 1 and value < root.left.value:
            return self.rightRotate(root)

        # right-right case
        if balance < -1 and value > root.right.value:
            return self.leftRotate(root)

        # left-right case
        if balance > 1 and value > root.left.value:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # right-left case
        if balance < -1 and value < root.right.value:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def balanceFactor(self, node):
        if node is None:
            return 0

        # leftHeight - rightHeight
        return self.getHeight(node.left) - self.getHeight(node.right)

    def getHeight(self, node):
        if node is None:
            return 0

        return node.height
    
    '''
    Reference for left rotation
            z
          y  t4
        x  t3
      t1 t2
    '''
    def leftRotate(self, z):
        y = z.left
        t3 = y.right

        y.right = z
        z.left = t3

        z.height = 1 + max( self.getHeight(z.left), self.getHeight(z.right) )
        y.height = 1 + max( self.getHeight(y.left), self.getHeight(y.right) )

        return y

    '''
    Reference for right rotation
            z
          t4   y
            t3   x
               t1 t2
    '''
    def rightRotate(self, z):
        y = z.right
        t3 = y.left

        y.left = z
        z.right = t3

        z.height = 1 + max( self.getHeight(z.left), self.getHeight(z.right) )
        y.height = 1 + max( self.getHeight(y.left), self.getHeight(y.right) )

        return y
