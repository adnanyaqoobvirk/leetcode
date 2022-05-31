class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def helper(pos: int) -> int:
            if pos < 0:
                return float('inf')

            if pos <= 1:
                return cost[pos]
            
            return cost[pos] + min(
                helper(pos - 1),
                helper(pos - 2)
            )
        cost.append(0)
        n = len(cost)
        return helper(n - 1)
        