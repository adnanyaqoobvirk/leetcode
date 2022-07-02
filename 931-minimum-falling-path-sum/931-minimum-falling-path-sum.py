class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        @cache
        def helper(row: int, col: int) -> int:
            if col < 0 or col >= n:
                return inf
            
            if row == n - 1:
                return matrix[row][col]
            
            return matrix[row][col] + min(
                helper(row + 1, col - 1),
                helper(row + 1, col),
                helper(row + 1, col + 1)
            )
        
        n = len(matrix)
        return min(helper(0, col) for col in range(n))