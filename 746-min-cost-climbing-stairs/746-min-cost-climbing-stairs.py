class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def helper(i: int) -> int:
            if i >= n:
                return 0
            
            if i not in memo:
                memo[i] = cost[i] + min(
                    helper(i + 1),
                    helper(i + 2)
                )
            return memo[i]
        
        n, memo = len(cost), {}
        return min(helper(0), helper(1))