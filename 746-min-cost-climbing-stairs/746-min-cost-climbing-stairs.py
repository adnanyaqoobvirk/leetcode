class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        n = len(cost)
        
        dp = [float('inf')] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for pos in range(2, n):
            dp[pos] = cost[pos] + min(
                dp[pos - 1],
                dp[pos - 2]
            )
        return dp[n - 1]