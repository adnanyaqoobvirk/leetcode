class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        distances = [[inf] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    distances[i][j] = 0
                    continue

                for x, y in [(i - 1, j), (i, j - 1)]:
                    if 0 <= x < m and 0 <= y < n:
                        distances[i][j] = min(distances[i][j], distances[x][y] + 1)
        
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if mat[i][j] == 0:
                    continue

                for x, y in [(i + 1, j), (i, j + 1)]:
                    if 0 <= x < m and 0 <= y < n:
                        distances[i][j] = min(distances[i][j], distances[x][y] + 1)

        return distances