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
        
        t1, t2 = getOrdered(root1), getOrdered(root2)
        p1, p2 = 0, len(t2) - 1
        while p1 < len(t1) and p2 >= 0:
            if t1[p1] + t2[p2] == target:
                return True
            
            if t1[p1] + t2[p2] < target:
                p1 += 1
            else:
                p2 -= 1
        return False
        
        