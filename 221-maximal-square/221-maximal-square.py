class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m, max_square = len(matrix), len(matrix[0]), 0
        prev_row, curr_row = [0] * m, [0] * m
        for i in range(n):
            for j in range(m):
                curr_row[j] = int(matrix[i][j])
                if curr_row[j]:
                    pi, pj = i - 1, j - 1
                    if 0 <= pi < n and 0 <= pj < m:
                        curr_row[j] += min(prev_row[j], curr_row[pj], prev_row[pj])
                max_square = max(max_square, curr_row[j])
            prev_row, curr_row = curr_row, prev_row
        return max_square * max_square