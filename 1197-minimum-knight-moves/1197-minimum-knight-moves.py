class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        @cache
        def helper(i: int, j: int) -> int:
            i, j = abs(i), abs(j)
            
            if i == 0 and j == 0:
                return 0
            
            if i + j == 2:
                return 2
            
            return 1 + min(
                helper(i - 1, j - 2),
                helper(i - 2, j - 1)
            )
        return helper(x, y)