class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root)
    inorder(root.right)

def preorder(root):
    if not root:
        return
    print(root)
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root)
