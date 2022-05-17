class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        ans, q = [[float('inf')] * n for _ in range(m)], []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                    ans[i][j] = 0
        while q:
            nq = []
            for i, j, d in q:
                for x, y in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]:
                    if 0 <= x < m and 0 <= y < n and ans[x][y] == float('inf'):
                        if mat[x][y] == 1:
                            ans[x][y] = d + 1
                            nq.append((x, y, d + 1))
            q = nq
        return ans