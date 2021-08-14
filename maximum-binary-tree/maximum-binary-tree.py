# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def buildTree(start: int, end: int) -> TreeNode:
            max_pos = None
            for i in range(start, end + 1):
                if max_pos is None:
                    max_pos = i
                elif nums[max_pos] < nums[i]:
                    max_pos = i
            if max_pos is not None:
                return TreeNode(
                    nums[max_pos], 
                    buildTree(start, max_pos - 1),
                    buildTree(max_pos + 1, end)
                )
        return buildTree(0, len(nums) - 1)