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
            
        negColumns = []
        posColumns = []
        q = [(root, 0)]
        while q:
            nq = []
            for curr, i in q:
                if i < 0:
                    if len(negColumns) < -i:
                        negColumns.append([])
                    negColumns[-i-1].append(curr.val)
                else:
                    if len(posColumns) < i + 1:
                        posColumns.append([])
                    posColumns[i].append(curr.val)
                if curr.left:
                    nq.append((curr.left, i - 1))
                if curr.right:
                    nq.append((curr.right, i + 1))
            q = nq
        return negColumns[::-1] + posColumns