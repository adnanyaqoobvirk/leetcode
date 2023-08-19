# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        outdegrees, parents, stack = {}, {root: None}, [root]
        while stack:
            curr = stack.pop()
                
            degree = 0
            if curr.left:
                degree += 1
                stack.append(curr.left)
                parents[curr.left] = curr
            
            if curr.right:
                degree += 1
                stack.append(curr.right)
                parents[curr.right] = curr
            
            outdegrees[curr] = degree
        
        ans, q = [], [curr for curr, degree in outdegrees.items() if degree == 0]
        while q:
            nq, level = [], []
            
            for curr in q:
                level.append(curr.val)
                
                parent = parents[curr]
                
                if parent:
                    outdegrees[parent] -= 1

                    if outdegrees[parent] == 0:
                        nq.append(parent)
            ans.append(level)
            q = nq
            
        return ans
                    