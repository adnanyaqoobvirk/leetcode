class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev, curr = cost[0], cost[1]
        for pos in range(2, n):
            prev, curr = curr, cost[pos] + min(
                curr,
                prev
            )
        return min(prev, curr)