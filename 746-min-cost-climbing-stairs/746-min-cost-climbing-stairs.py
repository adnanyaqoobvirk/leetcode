class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        curr = prev = 0
        for i in reversed(range(len(cost))):
            prev, curr = curr, cost[i] + min(curr, prev)
        return min(curr, prev)