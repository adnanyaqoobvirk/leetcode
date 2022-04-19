# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = deque()
        while root:
            if root.right:
                pre = root.right
                while pre.left and pre.left != root:
                    pre = pre.left
                
                if not pre.left:
                    pre.left = root
                    ans.appendleft(root.val)
                    root = root.right
                else:
                    pre.left = None
                    root = root.left
            else:
                ans.appendleft(root.val)
                root = root.left
        return ans