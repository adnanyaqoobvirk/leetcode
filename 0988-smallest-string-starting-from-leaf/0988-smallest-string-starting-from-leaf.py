# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def recurse(curr):
            if not curr:
                return ""

            s.append(chr(aval + curr.val))
            
            if not curr.left and not curr.right:
                ans = "".join(reversed(s))
                s.pop()
                return ans
            
            left = recurse(curr.left)
            right = recurse(curr.right)
            
            s.pop()

            if not left:
                return right
            elif not right:
                return left

            return min(left, right)
        
        s = []
        aval = ord("a")
        return recurse(root)