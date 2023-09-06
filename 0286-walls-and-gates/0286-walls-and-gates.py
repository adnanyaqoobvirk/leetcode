class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        
        q = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        d = 1
        while q:
            nq = []
            for i, j in q:
                for di, dj in directions:
                    x, y = i + di , j + dj
                    
                    if 0 <= x < m and 0 <= y < n and rooms[x][y] == 2147483647:
                        rooms[x][y] = d
                        nq.append((x, y))
            d += 1
            q = nq