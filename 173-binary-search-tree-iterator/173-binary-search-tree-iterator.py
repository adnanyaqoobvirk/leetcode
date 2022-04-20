# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack, self.root = [], root

    def next(self) -> int:
        while self.root:
            self.stack.append(self.root)
            self.root = self.root.left
        
        curr = self.stack.pop()
        res = curr.val
        if curr.right:
            self.root = curr.right
        return res
    
    def hasNext(self) -> bool:
        return self.stack or self.root

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()