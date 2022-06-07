class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        @cache
        def helper(i: int, j: int) -> int:
            if j < 0 or j == n:
                return float('inf')
            
            if i == n - 1:
                return matrix[i][j]
            
            return matrix[i][j] + min(
                helper(i + 1, j - 1),
                helper(i + 1, j),
                helper(i + 1, j + 1)
            )
        n = len(matrix)
        min_sum = float('inf')
        for j in range(n):
            min_sum = min(min_sum, helper(0, j))
        return min_sum