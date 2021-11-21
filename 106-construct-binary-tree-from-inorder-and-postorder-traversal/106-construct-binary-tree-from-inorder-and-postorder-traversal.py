class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(istart: int, iend: int) -> TreeNode:
            if istart <= iend:
                current = TreeNode(postorder.pop())
                
                ipos = inorder_map[current.val]
                
                current.right = helper(ipos + 1, iend)
                current.left = helper(istart, ipos - 1)
                
                return current
        inorder_map = {v: i for i, v in enumerate(inorder)}
        return helper(0, len(inorder) - 1)