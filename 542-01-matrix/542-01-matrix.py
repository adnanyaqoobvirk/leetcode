class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        ans = [[float('inf')] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                else:
                    minval = float('inf')
                    for x, y in [(i, j - 1), (i - 1, j)]:
                        if 0 <= x < m and 0 <= y < n:
                            minval = min(minval, ans[x][y])
                    ans[i][j] = min(ans[i][j], minval + 1)
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                minval = float('inf')
                for x, y in [(i, j + 1), (i + 1, j)]:
                    if 0 <= x < m and 0 <= y < n:
                        minval = min(minval, ans[x][y])
                ans[i][j] = min(ans[i][j], minval + 1)
        return ans