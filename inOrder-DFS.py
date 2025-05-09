def inOrder(root):
    if not root:
        return 
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)