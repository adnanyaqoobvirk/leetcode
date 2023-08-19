# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        col_map = defaultdict(list)
        q = [(root, 0)]
        while q:
            nq = []
            for curr, col in q:
                col_map[col].append(curr.val)
                
                if curr.left:
                    nq.append((curr.left, col - 1))
                
                if curr.right:
                    nq.append((curr.right, col + 1))
            q = nq
        return [col_map[i] for i in range(min(col_map), max(col_map) + 1)]