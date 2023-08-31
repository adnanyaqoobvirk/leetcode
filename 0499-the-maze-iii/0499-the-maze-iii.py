class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m, n = len(maze), len(maze[0])
        directions = [(1, 0, 'd'), (0, 1, 'r'), (-1, 0, 'u'), (0, -1, 'l')]
        
        visited = set()
        h = [(0, "", ball[0], ball[1])]
        while h:
            dis, p, i, j = heappop(h)
            
            if i == hole[0] and j == hole[1]:
                return p
            
            if (i, j) in visited:
                continue 
                    
            visited.add((i, j))
            
            for di, dj, dr in directions:
                x, y, ndis = i, j, dis
                
                while 0 <= x + di < m and 0 <= y + dj < n and maze[di + x][dj + y] == 0:
                    x += di
                    y += dj
                    ndis += 1
                    
                    if x == hole[0] and y == hole[1]:
                        break
                
                heappush(h, (ndis, p + dr, x, y))
                    
        return "impossible"