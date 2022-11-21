class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        entrance = (entrance[0], entrance[1])
        
        q = [entrance]
        seen = {entrance}
        steps = 0
        while q:
            nq = []
            for x, y in q:
                if (x, y) != entrance and (
                    x == 0 or x == m - 1 or y == 0 or y == n - 1
                ):
                    return steps
                for i, j in [
                    (x + 1, y), (x - 1, y),
                    (x, y + 1), (x, y - 1)
                ]:
                    cell = (i, j)
                    if 0 <= i < m and 0 <= j < n and maze[i][j] == '.' and cell not in seen:
                        nq.append(cell)
                        seen.add(cell)
            q = nq
            steps += 1
        return -1
                 