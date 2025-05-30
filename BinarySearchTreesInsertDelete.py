class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def insert(root, val):
    if not root:
        return  TreeNode(val)
    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)
    return root

def minValNode(root):       # Returns the min value node of a BST
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

def remove(root, val):
    if not root:
        return None
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            minNode = minValNode(root.right)
            root.val = minNode.val
            root.right = remove(root.right, minValNode.val)
        return root
