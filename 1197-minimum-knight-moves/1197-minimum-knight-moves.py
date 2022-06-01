class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        @cache
        def helper(i: int, j: int) -> int:
            if i == 0 and j == 0:
                return 0
            
            if i + j == 2:
                return 2
            
            return 1 + min(
                helper(abs(i - 1), abs(j - 2)),
                helper(abs(i - 2), abs(j - 1))
            )
        return helper(abs(x), abs(y))