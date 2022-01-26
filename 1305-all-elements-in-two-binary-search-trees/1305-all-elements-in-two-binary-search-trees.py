# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def helper(curr: TreeNode) -> None:
            if curr:
                helper(curr.left)
                ans.append(curr.val)
                helper(curr.right)
        
        ans = []
        helper(root1)
        r1_vals, ans = ans, []
        helper(root2)
        r2_vals = ans
        
        res = []
        p1 = p2 = 0
        while p1 < len(r1_vals) and p2 < len(r2_vals):
            if r1_vals[p1] < r2_vals[p2]:
                res.append(r1_vals[p1])
                p1 += 1
            else:
                res.append(r2_vals[p2])
                p2 += 1
        
        p, vals = (p1, r1_vals) if p1 < len(r1_vals) else (p2, r2_vals)
        while p < len(vals):
            res.append(vals[p])
            p += 1
            
        return res