class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def helper(pos: int) -> int:
            if pos < 0:
                return 0
            
            if pos == 1:
                return cost[pos]
            
            return min(
                cost[pos] + helper(pos - 2),
                cost[pos] + helper(pos - 1)
            )
        n = len(cost)
        return min(helper(n - 1), helper(n - 2))