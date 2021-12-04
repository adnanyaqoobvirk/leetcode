class Solution:
    def minCost(self, costs: List[List[int]]) -> int:    
        n = len(costs)
        dp = [[0] * 3 for _ in range(n + 1)]
        for i in range(n):
            for j in range(3):
                cost = float('inf')
                for k in range(3):
                    if k != j:
                        cost = min(cost, costs[i][k] + dp[i - 1][k])
                dp[i][j] = cost
        return min(dp[n - 1])