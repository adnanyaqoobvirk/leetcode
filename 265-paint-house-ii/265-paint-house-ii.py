class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n, k = len(costs), len(costs[0])
        prev, curr = [0] * k, [0] * k
        for house in reversed(range(n)):
            for rc in range(k):
                curr[rc] = float('inf')
                for c in range(k):
                    if c == rc:
                        continue
                    curr[rc] = min(curr[rc], prev[c])
                curr[rc] += costs[house][rc]
            prev, curr = curr, prev
        return min(prev)