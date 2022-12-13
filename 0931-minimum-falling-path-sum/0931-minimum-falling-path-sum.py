class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        @cache
        def helper(row, col):
            if row >= m or col < 0 or col >= n:
                return inf
            
            min_sum = min(
                helper(row + 1, col - 1),
                helper(row + 1, col),
                helper(row + 1, col + 1)
            )
            
            return matrix[row][col] + (min_sum if min_sum != inf else 0)
        
        m, n = len(matrix), len(matrix[0])
        return min(helper(0, c) for c in range(n))