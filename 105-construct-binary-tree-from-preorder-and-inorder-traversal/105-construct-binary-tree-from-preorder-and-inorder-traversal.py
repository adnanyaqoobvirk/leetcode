# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(left: int, right: int) -> TreeNode:
            if left > right:
                return None
            
            nonlocal ppos
            root_idx = idx_map[preorder[ppos]]
            root = TreeNode(preorder[ppos])
            ppos += 1
            
            root.left = helper(left, root_idx - 1)
            root.right = helper(root_idx + 1, right)
            
            return root
        
        ppos = 0
        idx_map = {num: i for i, num in enumerate(inorder)}
        return helper(0, len(inorder) - 1)