class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [
            [
                1 if j == n else 0
                for j in range(n + 1)
            ] 
            for i in range(6)
        ]
                    
        for i in range(4, -1, -1):
            for j in range(n - 1, -1, -1):
                for k in range(i, 5):
                    dp[i][j] += dp[k][j + 1]
        return dp[0][0]
                    