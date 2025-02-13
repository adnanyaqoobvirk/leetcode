# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        curr = root
        while curr:
            if not curr.left:
                ans.append(curr.val)
                curr = curr.right
            else:
                pre = curr.left

                while pre.right and pre.right != curr:
                    pre = pre.right
                
                if not pre.right:
                    pre.right = curr
                    curr = curr.left
                else:
                    ans.append(curr.val)
                    curr = curr.right
                    pre.right = None
        return ans