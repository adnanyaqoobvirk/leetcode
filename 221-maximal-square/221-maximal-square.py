class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m, max_square = len(matrix), len(matrix[0]), 0
        for i in range(n):
            for j in range(m):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j]:
                    pi, pj = i - 1, j - 1
                    if 0 <= pi < n and 0 <= pj < m:
                        matrix[i][j] += min(matrix[pi][j], matrix[i][pj], matrix[pi][pj])
                max_square = max(max_square, matrix[i][j])
        return max_square * max_square