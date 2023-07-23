class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        def recurse(i: int, j: int, c: int) -> int:
            if c == k:
                return 1
            
            if dp[i][j][c] != 0:
                return dp[i][j][c]
            
            total = 0
            for dr, dc in moves:
                ni, nj = i + dr, j + dc
                if 0 <= ni < n and 0 <= nj < n:
                    total += recurse(ni, nj, c + 1)
            
            dp[i][j][c] = total
            
            return total
            
        moves = [
            (-1, -2), (-2, -1), (-2, 1), (-1, 2),
            (1, -2), (2, -1), (2, 1), (1, 2)
        ]
        dp = [[[0] * k for _ in range(n)] for _ in range(n)]
        return recurse(row, column, 0) / 8 ** k