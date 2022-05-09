class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def helper(pos: int) -> int:
            if pos >= n:
                return 0
            
            return min(
                cost[pos] + helper(pos + 2),
                cost[pos] + helper(pos + 1)
            )
        n = len(cost)
        return min(helper(0), helper(1))