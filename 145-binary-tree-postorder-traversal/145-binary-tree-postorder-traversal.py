# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def reverse(f: Optional[TreeNode], t: Optional[TreeNode]) -> None:
            prev, curr = f, f.right
            while prev != t:
                node = curr.right
                curr.right = prev
                prev, curr = curr, node
        
        ans = []
        dummy = TreeNode(left=root)
        root = dummy
        while root:
            if root.left:
                node = root.left
                while node.right and node.right != root:
                    node = node.right
                
                if node.right:
                    reverse(root.left, node)
                    curr = node
                    while curr != root.left:
                        ans.append(curr.val)
                        curr = curr.right
                    ans.append(curr.val)
                    reverse(node, root.left)
                    node.right = None
                    root = root.right
                else:
                    node.right = root
                    root = root.left
            else:
                root = root.right
        return ans