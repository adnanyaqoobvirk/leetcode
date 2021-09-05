class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [
            [i if j == 0 else 1 for j in range(n)] 
            for i in range(1, 6)
        ]
        for i in range(1, 5):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        
        return dp[4][n - 1]
