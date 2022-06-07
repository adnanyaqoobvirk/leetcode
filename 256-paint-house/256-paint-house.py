class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        prev, curr = [0] * 3, [0] * 3
        for house in reversed(range(n)):
            for pcolor in range(3):
                curr[pcolor] = min(
                    costs[house][(pcolor + 1) % 3] + prev[(pcolor + 1) % 3],
                    costs[house][(pcolor + 2) % 3] + prev[(pcolor + 2) % 3]
                )
            prev, curr = curr, prev
        return min(prev)