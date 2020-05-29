# Average : O(log(n)) time | O(log(n)) space
# Worst: O(n) time | O(n) space
def findClosest(tree, target):
    findClosestHelper(tree, target, float("inf"))

def findClosestHelper(tree, target, closest):
    if tree is None:
        return closest

    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value

    if target < tree.value:
        findClosestHelper(tree.left, target, closest)
    elif target > tree.value:
        findClosestHelper(tree.right, target, closest)
    else:
        return closest

# Average : O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space 
def findClosestIterative(tree, target):
    iterativeWay(tree, target, float("inf"))
    
def iterativeWay(tree, target, closest):
    currentNode = tree

    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value

        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break

    return closest































