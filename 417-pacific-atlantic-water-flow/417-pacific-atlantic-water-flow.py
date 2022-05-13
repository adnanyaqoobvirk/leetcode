class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def helper(q: List[Tuple[int, int]], ocean: int) -> None:
            while q:
                nq = []
                for i, j in q:
                    nodes[(i, j)] |= ocean
                    for x, y in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]:
                        if 0 <= x < m and 0 <= y < n:
                            if nodes[(x, y)] & ocean != ocean and heights[x][y] >= heights[i][j]:
                                nq.append((x, y))
                q = nq

        m, n, nodes = len(heights), len(heights[0]), defaultdict(int)
        
        q = [(0, j) for j in range(n)]
        for i in range(1, m):
            q.append((i, 0))
        helper(q, 1)
        
        q = [(m - 1, j) for j in range(n)]
        for i in range(m - 1):
            q.append((i, n - 1))
        helper(q, 2)
        
        return [[i, j] for (i, j), v in nodes.items() if v == 3]
        