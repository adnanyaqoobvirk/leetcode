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
        
        col_map, q = defaultdict(list), [(root, 0)]
        min_col, max_col = float('inf'), float('-inf')
        while q:
            nq = []
            for node, col in q:
                col_map[col].append(node.val)
                min_col = min(min_col, col)
                max_col = max(max_col, col)
                
                if node.left:
                    nq.append((node.left, col - 1))
                if node.right:
                    nq.append((node.right, col + 1))
            q = nq
            
        return [col_map[col] for col in range(min_col, max_col + 1)]
        
        