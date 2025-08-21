class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        ans = 0
        counts = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if j == 0 or mat[i][j] == 0:
                    counts[i][j] = mat[i][j]
                else:
                    counts[i][j] = counts[i][j - 1] + 1
                
                minv = counts[i][j]
                for k in reversed(range(i)):
                    if minv == 0:
                        break
                    ans += minv
                    minv = min(minv, counts[k][j])
                ans += minv
        return ans