class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q, n, m = [], len(mat), len(mat[0])
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                else:
                    mat[i][j] = -1
        while q:
            nq = []
            for i, j, d in q:
                d += 1
                for x, y in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]:
                    if 0 <= x < n and 0 <= y < m and mat[x][y] == -1:
                        mat[x][y] = d
                        nq.append((x, y, d))
            q = nq
        return mat