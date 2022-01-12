# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        stack, curr, ans = [], root, []
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                node = stack.pop()
                ans.append(node.val)
                curr = node.right
        return ans