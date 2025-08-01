class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        for first in range(m // 2):
            last = m - 1 - first

            for c in range(first, last):
                offset = c - first

                top = matrix[first][c]
                matrix[first][c] = matrix[last - offset][first]
                matrix[last - offset][first] = matrix[last][last - offset]
                matrix[last][last - offset] = matrix[first + offset][last]
                matrix[first + offset][last] = top