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
        Idea is: The order of postorder is Left, Right, Root, but when you reverse it
        it becomes: root, right, left ( similar to preorder ), just left and right are reversed
        Therefore we will use this idea for postorder
    '''
    def iterativePostorder(self):
        if self is None:
            return

        ansStack = []
        tempStack = []

        currentNode = self
        while len(tempStack) or currentNode:

            if currentNode is not None:
                # Adding root
                ansStack.append(currentNode)
                tempStack.append(currentNode)
                # Going right
                currentNode = currentNode.right
            else:
                currentNode = tempStack.pop()
                # Going left
                currentNode = currentNode.left

        # Again reversing stack, for order Left, right, node
        for node in reversed(ansStack):
            print(node.value)

    '''
        Here, we will do level order traversal, i.e maintain a queue in which every element will
        contain [distance, currentNode].
        distance is, whenever we go left, we do distance.parent - 1, for right distance.parent + 1
        distance of root is 0, in below example, distance of 7 is -1, for 8, it is 0.
        Also we will maintain dictionary, where key will be the distance and value will be list of all node
        at that distance.
    '''
    
    def verticalOrderTraversal(self):
        queue = [  [0, self] ]
        distsToNodes = {}

        while len(queue):
            currentPair = queue.pop(0)
            distanceOfParent = currentPair[0]
            node = currentPair[1]

            # checking if distnace already exists in dictionary
            if distanceOfParent in distsToNodes:
                distsToNodes[distanceOfParent].append( node.value )
            else:
                # if not exists, then create a new list of node
                distsToNodes[distanceOfParent] = [node.value]

            # if left exists, then add that node to the queue
            if node.left:
                queue.append( [distanceOfParent - 1, node.left] )

            if node.right:
                queue.append( [distanceOfParent + 1, node.right] )

        sortTheDictByDistances = dict( sorted(distsToNodes.items(), key = lambda item :item[0] ) )
        for distance in sortTheDictByDistances:
            print(distance, ":", sortTheDictByDistances[distance])

    '''
        Idea is, use the vertical order traversal from above, and just update the dictionary only if distance not
        exist in it. 
    '''
    def topView(self):
        queue = [  [0, self] ]
        distsToNodes = {}

        while len(queue):
            currentPair = queue.pop(0)
            distanceOfParent = currentPair[0]
            node = currentPair[1]

            # checking if distnace not exists in dictionary, then add it, else igore it
            if distanceOfParent not in distsToNodes:
                distsToNodes[distanceOfParent] = node.value

            # if left exists, then add that node to the queue
            if node.left:
                queue.append( [distanceOfParent - 1, node.left] )

            if node.right:
                queue.append( [distanceOfParent + 1, node.right] )

        sortTheDictByDistances = dict( sorted(distsToNodes.items(), key = lambda item :item[0] ) )
        for distance in sortTheDictByDistances:
            print(distance, ":", sortTheDictByDistances[distance])

    '''
        Idea is, use vertical traversal from above, if the distance not exists in dict then add it, else if distance
        already exists then replace it's current value with the new value
    '''
    def bottomView(self):
        queue = [  [0, self] ]
        distsToNodes = {}

        while len(queue):
            currentPair = queue.pop(0)
            distanceOfParent = currentPair[0]
            node = currentPair[1]

            # checking if distnace already exists in dictionary, then just replace it's value with new value
            if distanceOfParent in distsToNodes:
                distsToNodes[distanceOfParent] = node.value
            else:
                # if not exists, then create add a node
                distsToNodes[distanceOfParent] = node.value

            # if left exists, then add that node to the queue
            if node.left:
                queue.append( [distanceOfParent - 1, node.left] )

            if node.right:
                queue.append( [distanceOfParent + 1, node.right] )

        sortTheDictByDistances = dict( sorted(distsToNodes.items(), key = lambda item :item[0] ) )
        for distance in sortTheDictByDistances:
            print(distance, ":", sortTheDictByDistances[distance])

    def spiralOrderTraversal(self):
        if self is None:
            return

        currentNode = self
        # 10 12 
        stack1 = [currentNode]
        stack2 = []

        while len(stack1) or len(stack2):
            while len(stack1):
                currentNode = stack1.pop()
                print(currentNode.value)
                
                if currentNode.left:
                    stack2.append(currentNode.left)

                if currentNode.right:
                    stack2.append(currentNode.right)

            while len(stack2):
                currentNode = stack2.pop()
                print(currentNode.value)

                if currentNode.right:
                    stack1.append(currentNode.right)

                if currentNode.left:
                    stack1.append(currentNode.left)


    '''
        idea is: path with max sum can be either left branch or right branch or left branch + right node + root
        e.g in below tree, 10                    10               10 
                          /                     /                 / \
                         7                     7                 7   12 is valid path 
                        / \                   /
                       6   8 is invalid path, 6 is valid path,
                                               
        At every time, if node is none, return [maxPathSumAsBranch, maxPathSumAsTriangle]
        
    '''

def maxPathSum(node):
    if node is None:
        return [0, 0]

    leftMaxBranchSumChild, leftMaxBranchSumIncludingRoot = maxPathSum(node.left)

    rightMaxBranchSumChild, rightMaxBranchSumIncludingRoot = maxPathSum(node.right)
    
    maxSumAsBranchChild = max(leftMaxBranchSumChild, rightMaxBranchSumChild)

    maxBranchIncludingRoot = max(maxSumAsBranchChild + node.value, node.value)

    maxSumAsTriangle = max(maxBranchIncludingRoot, leftMaxBranchSumChild + rightMaxBranchSumChild + node.value)

    maxSum = max(leftMaxBranchSumIncludingRoot, rightMaxBranchSumIncludingRoot, maxSumAsTriangle)

    return maxBranchIncludingRoot, maxSum
            
        
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

print("Vertical order traversal")
root.verticalOrderTraversal()

print("Top view of binary tree")
root.topView()

print("Bottom view of binary tree")
root.bottomView()

print("Max path sum")
print(maxPathSum(root))

print("Spiral Order Traversal")
root.spiralOrderTraversal()
