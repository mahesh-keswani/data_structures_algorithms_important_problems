# Time: O(n) and Space: O(n)
def branchSums(tree):
    sums = []
##                      tree, currentSum, list which will contain sum of all branches    
    calculateBranchSums(tree, 0, sums)

## Basically we are performing depth first search on tree
def calculateBranchSums(node, runningSum, sums):
##  i.e we have crossed the leaf  
    if node is None:
        return
    
    newRunningSum = runningSum + node.value

    if node.left is None and node.right is None:
        sums.append(newRunningSum)

    calculateBranchSums(node.left, newRunningSum, sums)
    calculateBranchSums(node.right, newRunningSum, sums)
    
