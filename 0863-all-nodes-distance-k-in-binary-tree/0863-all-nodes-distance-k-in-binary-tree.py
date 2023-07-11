# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph, q = defaultdict(list), [root]
        while q:
            nq = []
            for curr in q:
                if curr.left:
                    nq.append(curr.left)
                    graph[curr].append(curr.left)
                    graph[curr.left].append(curr)
                
                if curr.right:
                    nq.append(curr.right)
                    graph[curr].append(curr.right)
                    graph[curr.right].append(curr)
            q = nq
        
        q, vis, d = [target], {target}, 0
        while q:
            if d == k:
                break
                
            nq = []
            for curr in q:
                for nei in graph[curr]:
                    if nei not in vis:
                        nq.append(nei)
                        vis.add(nei)
            q, d = nq, d + 1
        return [curr.val for curr in q]