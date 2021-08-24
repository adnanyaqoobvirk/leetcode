class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        i = 0
        j = 0
        total = 0
        while i < n and j < m:
            total += mat[i][j]
            total += mat[i][m - j - 1]
            i += 1
            j += 1
        return total - mat[n // 2][m // 2] if n % 2 != 0 else total