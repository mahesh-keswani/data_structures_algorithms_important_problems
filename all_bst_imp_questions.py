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
    
    def converttoGraph(self):
        queue = deque()
        queue.append(self)

        while queue:
            node = queue.popleft()

            if 'children' not in node.__dict__:
                node.children = []

            if node.left:
                node.children.append(node.left)
                node.left.children = [node]
                queue.append(node.left)

            if node.right:
                node.children.append(node.right)
                node.right.children = [ node ]
                queue.append(node.right)
    
    # ides is first convert the binary tree into the graph and then perform bfs on the graph and return all the nodes which are at distance k from target
    def allNodesAtDistanceKFromTarget(self, target, k):
        queue = deque()
        queue.append( (target, 0) )

        visited = set()
        ans = []
        while queue:
            curr, dis = queue.popleft()

            if dis == k and curr not in visited:
                ans.append(curr.value)
            elif curr not in visited:
                for child in curr.children:
                    queue.append( (child, dis + 1) )

                visited.add(curr)

        return ans
	
	def getInorderArray(self, array):
        if self:

            if self.left:
                self.left.kthSmallestInBST(array)

            array.append(self.value)

            if self.right:
                self.right.kthSmallestInBST(array)

    # First performing the inorder traversal such that the elements will be sorted in the array
    # then simply returing kth smallest element
    def kthSmallestElement(self, k):
        array = []
        self.getInorderArray(array)
        return array[k]
        
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


def height(node):
    if node is None:
        return 0

    leftHeight = height(node.left)
    rightHeight = height(node.right)

    return max(leftHeight, rightHeight) + 1


def diameter(node):
    if node is None:
        return 0

    leftHeight = height(node.left)
    rightHeight = height(node.right)

    leftDiameter = diameter(node.left)
    rightDiameter = diameter(node.right)

    return max(leftDiameter, rightDiameter, leftHeight + rightHeight + 1)

def sortedArrayToBalancedBST(arr):
    n = len(arr)
    if n == 0:
        return None
    elif n == 1:
        return BST(arr[0])
    else:
        '''
            Idea is, take the middle element and make it as root (if n is even then take mid + 1 as root),
            then recursively call this function on left subarray and make it as left child of root, and
            recursively call this function on right subarray and make it as right child of root
        '''
        
        root = BST( arr[n // 2] )
        root.left = sortedArrayToBalancedBST( arr[: n//2] )
        
        # n//2 + 1 because, n//2 is root, and right subtree starts from n//2 + 1 to n
        root.right = sortedArrayToBalancedBST( arr[n//2 + 1:] )

        return root

def serialize(root, array):
	# for identification of leaf node, using -1 as a reference
    if root is None:
        array.append(-1)
        return

    array.append(root.value)
    serialize(root.left, array)
    serialize(root.right, array)

index = 0
def deserialize(array):
    if index == len(array) or array[index] == -1:
        index += 1
        return None

    root = BST(array[index])
    index += 1
    root.left = deserialize(array)
    root.right = deserialize(array)

    return root

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def preorder(self):
        if self:
            print(self.val, end = " ")

            if self.left:
                self.left.preorder()

            if self.right:
                self.right.preorder()
        
'''
    Given the inorder traversal find all possible binary trees.
    Idea is, consider every ith element as the root node and for every ith element recursively
    find left subtrees (from 0 to i-1) and right subtrees (from i+1 to n)and then make
    all possible combinations of leftSubtree, root and rightSubtree.
'''
        
def findAllTrees(inorder, start, end):
    # this will store all possible binary trees of given inorder traversal
    trees = []

    # i.e the subtree is empty
    if start >= end:
        trees.append(None)
        return None

    # if the subtree is not empty (i.e start <= end)
    for i in range(start, end):

        # find all left Subtrees
        leftTrees = findAllTrees(inorder, 0, i-1)

        # find all right subtrees
        rightTrees = findAllTrees(inorder, i+1, end)

        for leftTree in leftTrees:
            for rightTree in rightTrees:

                root = Node( inorder[i] )
                root.left = letfTree
                root.right = rightTree

                trees.append(root)

    return trees



inorder = [4, 6, 7]
trees = findAllTrees(0, len(inorder) - 1, inorder)
for tree in trees:
    tree.preorder()
    print()

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

print("Height")
print(height(root))

print("Diameter")
print(diameter(root))

print("Sorted array to BST")
arr = [1, 2, 3, 4, 5]
root = sortedArrayToBalancedBST(arr)
root.recursiveInorder()


'''
    We are given two arrays, from which if we construct BST then we have to check if the two bst's which will get formed
    are equal. But we are not allowed to actually construct BST and check if both of them are equal by using some
    traversal. So what we can do is check if both of them have different roots then both bsts are not equal.
    Also if lenghts of both arrays are different then also both are different bsts.
    If they have same root and also same lenght array, then check if the leftSubtree of the array's are equal.
    And similarly check if both of their right subtrees are equal.
'''

def sameBsts(array1, array2):
    if len(array1) != len(array2):
        return False

    # if the subtree's have 0 elements then both of them are equal 
    if len(array1) == 0 and len(array2) == 0:
        return True

    # both have different roots
    if array1[0] != array2[0]:
        return False

    # getting all the elements smaller than the root for the first array and all the elements >= root
    leftOne, rightOne = getSmallerAndBiggerOrEqual(array1)

    leftTwo, rightTwo = getSmallerAndBiggerOrEqual(array2)

    return sameBsts(leftOne, leftTwo) and sameBsts(rightOne, rightTwo)


def getSmallerAndBiggerOrEqual(array):
    smaller = []
    biggerOrEqual = []
    for i in range(1, len(array)):
        if array[i] < array[0]:
            smaller.append(array[i])
        elif array[i] >= array[0]:
            biggerOrEqual.append(array[i])

    return smaller, biggerOrEqual

'''
    Idea is, we will take every node as root, and check the number of nodes on the left and right side, then find
    total number of bst's possible for left subtree and right subtree.

    e.g say n=3, i.e we have 3 elements in bst, say{5, 6, 7}
    When 5 will be root, number of nodes on left=0 (index of 5), therefore number of bst's possible=1 (NULL TREE),
    on right we have 2 nodes, therefore number of bst's=2. Multiply both left*right
            +
    Now when 6 is root, no. of nodes on left=1 (index of 6), therefore no. of bst's possible=1
    on right no. of nodes=1, again bst's=1. Multiply left*right.
            +
    And same with root as 7
'''
def numberOfBSTPossibleWithNNodes(n):
    # initializing all the values as 0, index (i) will be no. of nodes in tree and it's value will be
    # number of possble bst's possible with i elements in tree.
    nBsts = [0 for i in range(n + 1)]

    # setting base conditions  
    nBsts[0] = 1
    nBsts[1] = 1
    nBsts[2] = 2

    # going from 3...n
    for i in range(3, n + 1):
        for j in range(0, i):
            # j represents the number of nodes of left, and i-j-1 represents number of nodes on right
            nBsts[i] = nBsts[i] + ( nBsts[j] * nBsts[i - j - 1] )

    return nBsts[-1]
    

'''
    In this, we will convert this bst to doublyLL using bfs traversal. 
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
def convertBstToDoublyLL(root):
    queue = [ root ]
    prevNode, head = None, None
    
    while queue:
        treeNode = queue.pop(0)
        node = Node( treeNode.value )
        
        if head is None:
            head = node
        else:
            node.prev = prevNode
            prevNode.next = node

        prevNode = node

        if node.left:
            queue.append( node.left )

        if node.right:
            queue.append( node.right )

    return head

'''
    In this, we will convert this bst to doublyLL using inorder traversal. 
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
def convertBstToDoublyLL(root):
    stack = []
    currentNode = root
    prevNode, head = None, None

    while currentNode or stack:
        if currentNode:
            stack.append( currentNode )
            currentNode = curentNode.left
        else:
            treeNode = stack.pop()
            node = Node( treeNode.value )

            if head is None:
                head = node
            else:
                node.prev = prevNode
                prevNode.next = node

            prevNode = node

            currentNode = treeNode.right

    return head

'''
    Idea is, we will perform dfs and add the element to the stack and will check if the node is leaf, then print
    all the ancestors from stack.
'''

# This stack is empty list
def allRootToLeafPaths(root, stack):
    
    if root:
        # before going to left, append node to stack
        stack.append( root )

        # basically performing recursive inorder 
        allRootToLeafPaths(root.left, stack)

        # if leaf is reached, then print it's path
        if root.left is None and root.right is None:
            for node in stack:
                print(node.value, end = ' ')
                
            # For going to the new line
            print()
        
        allRootToLeafPaths( root.right, stack )

        # once the element is processed, remove it from the stack.
        stack.pop()

def checkIfTwoTreesAreSymmetric(root1, root2):
    # if both the roots are null, then they are symmetric (hypothetically)
    if root1 is None and root2 is None:
        return True

    # if one of the root is none and other is not, then it is not symmetric
    if root1 is None or root2 is None:
        return False

    # if the root1 data != root2 data, then there is no need to check further. 
    if root1.data != root2.data:
        return False

    # For the two trees to be symmetric, left subtree of root1 should be same as right subtree of root2
    # and right subtree of root1 should be same as left subtree of root2
    return checkIfTwoTreesAreSymmetric(root1.left, root2.right) and checkIfTwoTreesAreSymmetric(root1.right, root2.left)

# nextRight property is to point to the nearest node in the same level, if node exists.
class BinaryTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.nextRight = None

def populateNextRightPointers(root):
    # here we will do level order traversal to populate nextRight pointers
    queue = [ root ]
    while queue:
        currentSize = len(queue)

        for i in range(currentSize):
            node = queue.pop(0)

            # if we have more than 1 element in the queue
            # (i.e there are few more nodes in the same level), then set their nextRight pointers
            if i < (currentSize - 1):
                node.nextRight = queue[0] or None

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
    return root


'''
every branch collectively form one number, we have to return sum of all numbers.

       5
      /  \ 
    4     7
   / \     \ 
   1 2     8
      \
       3

ans = 541 + 5423 + 578

'''
def rootToLeafSum(root, val = 0):
    if root is None:
        return 0

    val = ( val * 10 ) + root.value
    return rootToLeafSum(root.left, val) + rootToLeafSum(root.right, val)

'''
    We have to find the sum of all the nodes at the maximum depth.

    Idea is: Just perform the bfs, for every level, initialize the sum as 0 and calculate the sum.
    When the last level is completely traversed, the sum of all nodes at max depth will be stored
    in sum.
'''
def sumOfNodesAtMaxDepth(root):
    queue = [root]

    sum = 0
    while queue:
        # we are basically calculating sum for every level, when the last level is completely
        # traversed, sum will be caluclated and queue will be empty.
        sum = 0
        size = len(queue)

        for i in range(size):
            node = queue.pop(0)
            sum += node.value

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    return sum

'''
    Given a tree, check if all the leaves are at same level.
    Idea is simple, calculate the height of one leaf, if all the leaves have the same height then
    return true, else false.
'''
def checkSameHeight(root):
    # for storing the height of the tree
    treeHeight = {'height': 0}
    return checkSameHeightHelper(root, 0, treeHeight)

def checkSameHeightHelper(root, currentHeight, treeHeight):
    if root is None:
        return True

    if root.left is None and root.right is None:

        # when the leaf node is reached for the first time
        if treeHeight['height'] == 0:
            treeHeight['height'] = currentHeight
            return True
        else:
            return currentHeight == treeHeight['height']

    # if the leaf is not reached, check for the left and right subtrees
    left = checkSameHeightHelper(root.left, currentHeight + 1, treeHeight)
    right = checkSameHeightHelper(root.right, currentHeight + 1, treeHeight)

    return left and right
'''
	Idea is, first we will collect all the paths in the stack and once the leaf is reached, we will traverse the path backwards, and check continously if the
	sum is equal to k, if yes, then we will store the path from ith index to end of stack in result. (as we are traversing backwards)
'''
def kPathSums( root, k ):
	result = []
	kPathSumsHelper( root, k, [], result )
	return result

def kPathSumsHelper( root, k, stack, result ):
	if root is None:
		return
	
	# perform inorder traversal
	stack.append( root )
	kPathSumsHelper( root.left, k, stack, result )
	
	# if leaf is reached
	if root.left is None and root.right is None:
		currentSum = 0
		for i in range(len(stack) - 1, -1, -1):
			currentSum = currentSum + stack[i]
			
			if currentSum == k:
				# store the path from i to end in result
				result.append( stack[i:] )
			
			# Don't break the break as there might be negative numbers which may again lead to sum as k
	
	kPathSumsHelper( root.right, k, stack, result )
	
	# once the element is completely processed, remove it from stack
	stack.pop()


def replaceNodeWithSumOfItsDescendents(root):

    if root is None:
        return 0

    # if the node is leaf, we don't want to do anything, just pass it's value to the parent
    if root.left is None and root.right:
        return root.value

    # store the value of the root, as it is going to be updated and we have to pass it's value
    # to the parent as well.
    nodeValue = root.value

    # basically doing postorder traversal
    leftSum = replaceNodeWithSumOfItsDescendents(root.left)
    rightSum = replaceNodeWithSumOfItsDescendents(root.right)

    # update the node with sum of its left and right subtrees
    root.value = leftSum + rightSum

    return nodeValue + root.value







