# Time: O(n) and space: O(d), d = depth of tree for all traversals
def inorder(tree):
    if tree is not None:
        inorder(tree.left)
        print(tree.value)
        inorder(tree.right)

def preorder(tree):
    if tree is not None:
        print(tree.value)
        inorder(tree.left)
        inorder(tree.right)
        
def postorder(tree):
    if tree is not None:
        inorder(tree.left)
        inorder(tree.right)
        print(tree.value)
