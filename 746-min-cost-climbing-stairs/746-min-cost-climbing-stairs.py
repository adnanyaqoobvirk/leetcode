class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev, curr = inf, 0
        for pos in reversed(range(len(cost))):
            prev, curr = curr, cost[pos] + min(prev, curr)
        return min(prev, curr)