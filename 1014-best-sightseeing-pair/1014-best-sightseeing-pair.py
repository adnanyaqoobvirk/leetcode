class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        
        dp = [[-inf] * 2 for _ in range(n)]
        dp[n - 1][1] = values[n - 1] - n + 1
        
        for pos in reversed(range(n - 1)):
            dp[pos][1] = max(
                values[pos] - pos,
                dp[pos + 1][1]
            )
            dp[pos][0] = max(
                dp[pos + 1][0],
                values[pos] + pos + dp[pos + 1][1]
            )
        return dp[0][0]