# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.vals, self.nxt, stack = [], -1, []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                curr = stack.pop()
                self.vals.append(curr.val)
                if curr.right:
                    root = curr.right

    def next(self) -> int:
        self.nxt += 1
        return self.vals[self.nxt]

    def hasNext(self) -> bool:
        return self.nxt + 1 < len(self.vals)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()