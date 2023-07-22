class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        @cache
        def dp(i: int, j: int, c: int) -> int:
            if c == k:
                return 1
            
            total = 0
            for dr, dc in moves:
                ni, nj = i + dr, j + dc
                if 0 <= ni < n and 0 <= nj < n:
                    total += dp(ni, nj, c + 1)
                    
            return total
            
        moves = [
            (-1, -2), (-2, -1), (-2, 1), (-1, 2),
            (1, -2), (2, -1), (2, 1), (1, 2)
        ]
        return dp(row, column, 0) / (8 ** k)