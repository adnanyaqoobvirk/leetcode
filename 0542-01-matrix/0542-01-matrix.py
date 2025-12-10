class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        distances = [[0] * n for _ in range(m)]
        q = [(i, j) for i in range(m) for j in range(n) if mat[i][j] == 0]
        seen = set(q)
        steps = 0
        while q:
            steps += 1
            nq = []
            for i, j in q:
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= x < m and 0 <= y < n and (x, y) not in seen and mat[x][y] != 0:
                        seen.add((x, y))
                        nq.append((x, y))
                        distances[x][y] = steps
            q = nq
        return distances