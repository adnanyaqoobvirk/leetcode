class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        mid = n // 2
        total = 0
        for i in range(n):
            total += mat[i][i] + mat[i][m - i - 1]
        return total if n % 2 == 0 else total - mat[mid][mid]