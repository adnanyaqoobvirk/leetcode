class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @cache
        def helper(a: int, b: int) -> int:
            ans = 0
            for x, y in directions:
                x, y = a + x, b + y
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[a][b]:
                    ans = max(ans, helper(x, y))
            return ans + 1
        
        m, n = len(matrix), len(matrix[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        return max(
            helper(i, j)
            for i in range(m)
            for j in range(n)
        )
                