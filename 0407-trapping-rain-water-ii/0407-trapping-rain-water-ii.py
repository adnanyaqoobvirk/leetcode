class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        h = []
        seen = set()
        for j in range(n):
            h.append((heightMap[0][j], 0, j))
            seen.add((0, j))
            h.append((heightMap[m - 1][j], m - 1, j))
            seen.add((m - 1, j))
        for i in range(m):
            h.append((heightMap[i][0], i, 0))
            seen.add((i, 0))
            h.append((heightMap[i][n - 1], i, n - 1))
            seen.add((i, n - 1))
        heapify(h)

        ans = 0
        while h:
            height, i, j = heappop(h)
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in seen:
                    if heightMap[x][y] < height:
                        ans += height - heightMap[x][y]
                        heappush(h, (height, x, y))
                    else:
                        heappush(h, (heightMap[x][y], x, y))
                    seen.add((x, y))
        return ans
            

