class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        nodes = set(range(n))
        for a, b in edges:
            nodes.discard(b)
        return next(iter(nodes)) if len(nodes) == 1 else -1