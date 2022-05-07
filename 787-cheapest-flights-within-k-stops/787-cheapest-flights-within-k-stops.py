class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prev = defaultdict(lambda: float('inf'))
        prev[src] = 0
        for _ in range(k + 1):
            curr = defaultdict(lambda: float('inf'))
            curr[src] = 0
            for s, d, p in flights:
                curr[d] = min(curr[d], prev[s] + p)
            prev = curr
        return -1 if prev[dst] == float('inf') else prev[dst]