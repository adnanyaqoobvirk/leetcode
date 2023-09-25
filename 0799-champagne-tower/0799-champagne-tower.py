class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        @cache
        def dp(i: int, j: int) -> float:
            if i == 0 and j == 0:
                return poured
            
            if i < 0 or j < 0:
                return 0
            
            return max(0, dp(i - 1, j) - 1) / 2 + max(0, dp(i - 1, j - 1) - 1) / 2
        return min(1, dp(query_row, query_glass))