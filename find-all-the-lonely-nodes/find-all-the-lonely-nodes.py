# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        def recurse(current: TreeNode) -> None:
            if current:
                if current.right and not current.left:
                    output.append(current.right.val)
                elif current.left and not current.right:
                    output.append(current.left.val)

                recurse(current.left)
                recurse(current.right)
                
        output = []
        recurse(root)
        return output