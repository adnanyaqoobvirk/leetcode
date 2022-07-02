class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        cmat = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                cmat[i][j] = (
                    mat[i - 1][j - 1] + cmat[i - 1][j] - cmat[i - 1][j - 1] + cmat[i][j - 1]
                )
        
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1, c1 = max(i - k, 0) + 1, max(j - k, 0) + 1
                r2, c2 = min(i + k, m - 1) + 1, min(j + k, n - 1) + 1
                
                ans[i][j] = (
                    cmat[r2][c2] - cmat[r1 - 1][c2] - cmat[r2][c1 - 1] + cmat[r1 - 1][c1 - 1]
                )
        return ans