class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m, n = len(maze), len(maze[0])
        dmap = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        cmap = ['d', 'r', 'u', 'l']
        
        seen = set()
        q = [(ball[0], ball[1], d, ()) for d in range(len(dmap))]
        res = ""
        finished = False
        while q and not finished:
            nq = []
            
            for i, j, d, path in q:
                if i == hole[0] and j == hole[1]:
                    finished = True
                    ins = "".join(cmap[c] for c in path)
                    if not res or ins < res:
                        res = ins
                
                if finished:
                    continue
                
                seen.add((i, j, d))
                di, dj = dmap[d]
                x, y = i + di, j + dj
                
                if not (0 <= x < m and 0 <= y < n) or maze[x][y] == 1:
                    for k, (di, dj) in enumerate(dmap):
                        a, b = di + i, dj + j
                        
                        if 0 <= a < m and 0 <= b < n and maze[a][b] != 1 and (a, b, k) not in seen:
                            nq.append((a, b, k, path + (k,)))
                elif (x, y, d) not in seen:
                    nq.append((x, y, d, path + (d,)))
            q = nq
        
        ans = []
        prev = ""
        for curr in res:
            if prev != curr:
                ans.append(curr)
            prev = curr
        return "".join(ans) if ans else "impossible"