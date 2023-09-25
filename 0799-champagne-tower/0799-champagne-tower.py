class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * 101 for _ in range(101)]
        for i in range(query_row + 1):
            for j in range(i + 1):
                if i == 0 and j == 0:
                    dp[i][j] = poured
                else:
                    dp[i][j] = max(0, dp[i - 1][j] - 1) / 2 + max(0, dp[i - 1][j - 1] - 1) / 2
        return min(1, dp[query_row][query_glass])