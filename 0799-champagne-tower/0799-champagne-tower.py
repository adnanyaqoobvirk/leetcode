class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * 101 for _ in range(101)]
        dp[0][0] = poured
        for i in range(1, query_row + 1):
            for j in range(i + 1):
                dp[i][j] = max(0, dp[i - 1][j] - 1) / 2 + max(0, dp[i - 1][j - 1] - 1) / 2
        return min(1, dp[query_row][query_glass])