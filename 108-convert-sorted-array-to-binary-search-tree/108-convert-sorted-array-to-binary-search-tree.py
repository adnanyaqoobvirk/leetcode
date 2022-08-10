# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def recurse(left: int, right: int) -> TreeNode:
            if left < right:
                mid = (right - left) // 2 + left
                root = TreeNode(nums[mid])
                root.right = recurse(mid + 1, right)
                root.left = recurse(left, mid)
                return root
        
        return recurse(0, len(nums))