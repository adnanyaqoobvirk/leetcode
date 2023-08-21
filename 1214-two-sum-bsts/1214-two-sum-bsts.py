# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        stack = [root1]
        while stack:
            curr1 = stack.pop()
            
            if not curr1:
                continue
            
            diff = target - curr1.val
            curr2 = root2
            while curr2:
                if curr2.val == diff:
                    return True
                
                if curr2.val < diff:
                    curr2 = curr2.right
                else:
                    curr2 = curr2.left
                    
            stack.append(curr1.right)
            stack.append(curr1.left)
        return False