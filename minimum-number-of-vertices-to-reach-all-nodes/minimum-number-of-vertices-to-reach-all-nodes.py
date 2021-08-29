class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        to_nodes = {t for f, t in edges}
        return {f for f, t in edges if f not in to_nodes}