# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def helper(curr: Optional[TreeNode]) -> None:
            if curr:
                nonlocal start_path, dest_path
                
                if curr.val == startValue:
                    start_path = path[::-1]
                elif curr.val == destValue:
                    dest_path = path[::-1]
                    
                if not start_path or not dest_path:
                    path.append("L")
                    helper(curr.left)
                    path.pop()

                    path.append("R")
                    helper(curr.right)
                    path.pop()
                
        path, start_path, dest_path = [], None, None
        helper(root)
        
        while start_path and dest_path and start_path[-1] == dest_path[-1]:
            start_path.pop()
            dest_path.pop()
        
        ans = ["U"] * len(start_path)
        ans.extend(reversed(dest_path))
        return "".join(ans)
                