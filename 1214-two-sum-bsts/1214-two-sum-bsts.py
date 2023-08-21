# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def getOrdered(curr: Optional[TreeNode]) -> List[int]:
            res, stack = [], []
            while curr or stack:
                if curr:
                    stack.append(curr)
                    curr = curr.left
                else:
                    curr = stack.pop()
                    res.append(curr.val)
                    curr = curr.right
            return res
        
        t2 = set(getOrdered(root2))
        for v in getOrdered(root1):
            if target - v in t2:
                return True
        return False
        