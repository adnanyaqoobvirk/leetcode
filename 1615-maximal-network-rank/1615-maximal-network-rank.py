class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        connections, sroads = defaultdict(int), set()
        for src, dst in roads:
            sroads.add((min(src, dst), max(src, dst)))
            connections[src] += 1
            connections[dst] += 1
        
        max_rank = 0
        for i in range(n):
            for j in range(i + 1, n):
                rank = connections[i] + connections[j]
                if (i, j) in sroads:
                    rank -= 1
                max_rank = max(max_rank, rank)
        return max_rank