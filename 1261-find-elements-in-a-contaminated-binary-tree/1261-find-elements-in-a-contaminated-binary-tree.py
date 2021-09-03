# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        def recurse(current: TreeNode, val: int) -> None:
            if current:
                if current.left:
                    left = val * 2 + 1
                    self.vals.add(left)
                    recurse(current.left, left)
                if current.right:
                    right = val * 2 + 2
                    self.vals.add(right)
                    recurse(current.right, right)
        self.vals = {0}
        recurse(root, 0)
        
    def find(self, target: int) -> bool:
        return target in self.vals


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)