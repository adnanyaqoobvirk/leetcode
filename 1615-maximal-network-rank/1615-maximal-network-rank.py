class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        for src, dst in roads:
            graph[src].add(dst)
            graph[dst].add(src)
          
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                ans = max(ans, len(graph[i]) + len(graph[j]) - int(i in graph[j]))
        return ans