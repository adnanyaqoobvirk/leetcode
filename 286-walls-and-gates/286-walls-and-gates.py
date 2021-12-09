class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        n, m = len(rooms), len(rooms[0])
        q = []
        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    q.append((i, j))
        d = 0
        while q:
            d += 1
            nq = []
            for i, j in q:
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= x < n and 0 <= y < m and rooms[x][y] == 2147483647:
                        rooms[x][y] = d
                        nq.append((x, y))
            q = nq