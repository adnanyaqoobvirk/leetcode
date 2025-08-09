class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 10000:
            return 1

        n = ceil(n / 25) + 1
        turns = [(4, 0), (3, 1), (2, 2), (1, 3)]
        dp = [[0] * n for _ in range(n)]
        dp[0][0] = 0.5
        for i in range(1, n):
            dp[0][i] = 1
        for a in range(1, n):
            for b in range(1, n):
                for da, db in turns:
                    dp[a][b] += dp[max(a - da, 0)][max(b - db, 0)]
                dp[a][b] *= 0.25
        return dp[n - 1][n - 1]