class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        graph, outdegrees = defaultdict(list), defaultdict(int)
        for i in range(m):
            for j in range(n):
                for x, y in directions:
                    x, y = i + x, j + y
                    if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                        graph[(x, y)].append((i, j))
                        outdegrees[(i, j)] += 1
        
        q = [
            (i, j) 
            for i in range(m) 
            for j in range(n) 
            if outdegrees[(i, j)] == 0
        ]
        ans = 0
        while q:
            nq = []
            for i, j in q:
                for x, y in graph[(i, j)]:
                    outdegrees[(x, y)] -= 1
                    if outdegrees[(x, y)] == 0:
                        nq.append((x, y))
            q = nq
            ans += 1
        return ans