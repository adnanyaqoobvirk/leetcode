class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegrees = defaultdict(int)
        for src, dst in edges:
            indegrees[dst] += 1
        return [node for node in range(n) if indegrees[node] == 0]
        
        