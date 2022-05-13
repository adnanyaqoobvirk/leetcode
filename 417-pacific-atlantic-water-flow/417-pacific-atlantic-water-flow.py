class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def helper(stack: List[Tuple[int, int]], ocean: int) -> None:
            while stack:
                i, j = stack.pop()
                nodes[(i, j)] |= ocean
                for x, y in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]:
                    if 0 <= x < m and 0 <= y < n:
                        if nodes[(x, y)] & ocean != ocean and heights[x][y] >= heights[i][j]:
                            stack.append((x, y))

        m, n, nodes = len(heights), len(heights[0]), defaultdict(int)
        
        stack = [(0, j) for j in range(n)]
        for i in range(1, m):
            stack.append((i, 0))
        helper(stack, 1)
        
        stack = [(m - 1, j) for j in range(n)]
        for i in range(m - 1):
            stack.append((i, n - 1))
        helper(stack, 2)
        
        return [[i, j] for (i, j), v in nodes.items() if v == 3]
        