class ListNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def search(root, target):
    if not root:
        return False
    if target > root:
        return search(root.right, target)
    elif target < root:
        return search(root.left, target)
    else: return True
        
    
        