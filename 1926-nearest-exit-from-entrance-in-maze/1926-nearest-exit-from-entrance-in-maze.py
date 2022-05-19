class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n, (ex, ey) = len(maze), len(maze[0]), entrance
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        maze[ex][ey] = '-'
        ans, q = 0, [(ex, ey)]
        while q:
            nq = []
            for i, j in q:
                for x, y in directions:
                    x, y = i + x, j + y
                    if 0 <= x < m and 0 <= y < n:
                        if maze[x][y] == '.':
                            maze[x][y] = '-'
                            nq.append((x, y))
                    elif i != ex or j != ey:
                        return ans
            ans += 1
            q = nq
        return -1