class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [
            (-1, -2), (-2, -1), (-2, 1), (-1, 2),
            (1, -2), (2, -1), (2, 1), (1, 2)
        ]
        dp = [[[0] * (k + 1) for _ in range(n)] for _ in range(n)]
        
        for c in reversed(range(k + 1)):
            for j in range(n):
                for i in range(n):
                    if c == k:
                        dp[i][j][c] = 1
                        continue
                
                    total = 0
                    for dr, dc in moves:
                        ni, nj = i + dr, j + dc
                        if 0 <= ni < n and 0 <= nj < n:
                            total += dp[ni][nj][c + 1]

                    dp[i][j][c] = total
        return dp[row][column][0] / (8 ** k)