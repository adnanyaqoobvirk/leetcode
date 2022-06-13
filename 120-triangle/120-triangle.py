class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        def helper(row: int, col: int) -> int:
            if row == n - 1:
                return triangle[row][col]
            
            return triangle[row][col] + min(
                helper(row + 1, col),
                helper(row + 1, col + 1)
            )
        
        n = len(triangle)
        return helper(0, 0)