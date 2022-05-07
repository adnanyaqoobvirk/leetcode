class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        heap, nodes = [(0, 0, 0)], {}
        while heap:
            effort, i, j = heappop(heap)
            if (i, j) not in nodes:
                nodes[(i, j)] = effort
                for x, y in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]:
                    if 0 <= x < m and 0 <= y < n:
                        heappush(
                            heap, 
                            (
                                max(effort, abs(heights[i][j] - heights[x][y])),
                                x,
                                y
                            )
                        )
        return nodes[(m - 1, n - 1)]