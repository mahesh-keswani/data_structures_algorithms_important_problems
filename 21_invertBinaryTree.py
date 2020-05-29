# Time: O(n) and space: O(n), because at some stage the queue will contain all the leaves 
def invertBinaryTree(tree):
    queue = [tree]
    while len(queue):
        currentNode = queue.pop(0)

        if currentNode is None:
            continue
        else:
            swapLeftAndRight(currentNode)
            queue.append(currentNode.left)
            queue.append(currentNode.right)
            
def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left

# Time: O(n) and space: O(d), d = depth of the tree
def invertBinaryTree(tree):
    if tree is None:
        return
    else:
        swapLeftAndRight(tree)
        invertBinaryTree(tree.left)
        invertBinaryTree(tree.right)
        
def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left      
