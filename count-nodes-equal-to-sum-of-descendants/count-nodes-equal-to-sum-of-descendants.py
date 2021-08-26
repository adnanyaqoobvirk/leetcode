# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        def recurse(current: TreeNode) -> int:
            nonlocal count
            
            result = 0
            if current:
                result += recurse(current.left)
                result += recurse(current.right)
                
                if result == current.val:
                    count += 1
                result += current.val
            return result
        
        count = 0
        recurse(root)
        return count