# Time: O(n) and space: O(d), d = depth of the tree
def validateBST(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))

def validateBstHelper(tree, minValue, maxValue):
    if tree is None:
        return True

    if tree.value < minValue or tree.value > maxValue:
        return False
    else:
        validateLeftBST = validateBstHelper(tree.left, minValue, tree.value)
        validateRightBST = validateBstHelper(tree.right, tree.value, maxValue)

        return validateLeftBST and validateRightBST
