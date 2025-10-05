class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        
        pq, aq = [], []
        pseen, aseen = set(), set()
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    pq.append((i, j))
                    pseen.add((i, j))
                if i == m - 1 or j == n - 1:
                    aq.append((i, j))
                    aseen.add((i, j))
        
        status = defaultdict(int)

        while pq:
            nqp = []
            for i, j in pq:
                status[(i, j)] |= 1
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= x < m and 0 <= y < n and (x, y) not in pseen and heights[x][y] >= heights[i][j]:
                        nqp.append((x, y))
                        pseen.add((x, y))
            pq = nqp
        
        while aq:
            nap = []
            for i, j in aq:
                status[(i, j)] |= 2
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= x < m and 0 <= y < n and (x, y) not in aseen and heights[x][y] >= heights[i][j]:
                        nap.append((x, y))
                        aseen.add((x, y))
            aq = nap
        
        ans = []
        for idx, v in status.items():
            if v == 3:
                ans.append(idx)
        return ans