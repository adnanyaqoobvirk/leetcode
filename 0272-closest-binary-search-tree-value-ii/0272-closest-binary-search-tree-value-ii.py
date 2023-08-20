# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        inorder, stack, left, diff = [], [], None, inf
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                inorder.append(root.val)
                curr_diff = abs(root.val - target)
                if curr_diff < diff:
                    left = len(inorder) - 1
                    diff = curr_diff
                root = root.right
        
        ans, right = [], left + 1
        while k > 0:
            if left < 0:
                ans.append(inorder[right])
                right += 1
            elif right >= len(inorder):
                ans.append(inorder[left])
                left -= 1
            else:
                if abs(inorder[left] - target) < abs(inorder[right] - target):
                    ans.append(inorder[left])
                    left -= 1
                else:
                    ans.append(inorder[right])
                    right += 1
            k -= 1
        return ans
        