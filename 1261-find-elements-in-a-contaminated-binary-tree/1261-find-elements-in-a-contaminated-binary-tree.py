# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        self.vals = set()
        stack = [root]
        while stack:
            current = stack.pop()
            self.vals.add(current.val)
            if current.left:
                current.left.val = current.val * 2 + 1
                stack.append(current.left)
            if current.right:
                current.right.val = current.val * 2 + 2
                stack.append(current.right)
        
    def find(self, target: int) -> bool:
        return target in self.vals


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)