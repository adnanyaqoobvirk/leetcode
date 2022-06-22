class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        
        total = 0
        for rc in range(n):
            total += mat[rc][rc]
            if rc != n - rc - 1:
                total += mat[rc][n - rc - 1]
        return total