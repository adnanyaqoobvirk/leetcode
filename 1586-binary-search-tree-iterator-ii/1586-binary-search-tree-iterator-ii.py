# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.nxt = -1
        self.vals, stack = [], []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                curr = stack.pop()
                self.vals.append(curr.val)
                if curr.right:
                    root = curr.right
                    
    def hasNext(self) -> bool:
        return self.nxt + 1 < len(self.vals)

    def next(self) -> int:
        self.nxt += 1
        return self.vals[self.nxt]

    def hasPrev(self) -> bool:
        return self.nxt > 0

    def prev(self) -> int:
        self.nxt -= 1
        return self.vals[self.nxt]


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()