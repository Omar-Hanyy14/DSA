class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.right = self.left = None

    def enqueue(self, val):
        newNode = ListNode(val)
        # Queue is not empty
        if self.right:
            self.right.next = newNode
            self.right = self.right.next
        # Queue is empty
        else:
            self.left = self.right = newNode



    def dequeue(self):
        # Queue is empty
        if not self.left:
            return None
        # Remove left node and return value
        val = self.left.val
        self.left = self.left.next
        if not self.left:
            self.right = None
        return val
    
    def print(self):
        curr = self.left
        while curr:
            print(curr.val, ' -> ', end="")
            curr = curr.next
        print() # New Line
