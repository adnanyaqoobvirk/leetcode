# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        tilt_sum, stack, processed = 0, [root], defaultdict(int)
        while stack:
            curr = stack[-1]
            
            if curr not in processed:
                if curr.right:
                    stack.append(curr.right)

                if curr.left:
                    stack.append(curr.left)
                    
                processed[curr] = 0
            else:
                stack.pop()
                
                left_sum, right_sum = processed[curr.left], processed[curr.right]
                
                tilt_sum += abs(left_sum - right_sum)
                
                processed[curr] = curr.val + left_sum + right_sum
        return tilt_sum
                
            
            
            