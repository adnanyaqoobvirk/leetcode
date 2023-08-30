class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        dmap = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        seen = set()
        q = [(start[0], start[1], d) for d in range(len(dmap))]
        distance = 0
        while q:
            nq = []
            
            for i, j, d in q:
                di, dj = dmap[d]
                x, y = i + di, j + dj
                
                if not (0 <= x < m and 0 <= y < n) or maze[x][y] == 1:
                    if i == destination[0] and j == destination[1]:
                        return distance
                
                    for k, (di, dj) in enumerate(dmap):
                        a, b = di + i, dj + j
                        
                        if 0 <= a < m and 0 <= b < n and maze[a][b] != 1 and (a, b, k) not in seen:
                            seen.add((a, b, k))
                            nq.append((a, b, k))
                elif (x, y, d) not in seen:
                    seen.add((x, y, d))
                    nq.append((x, y, d))
            q = nq
            distance += 1
            
        return -1