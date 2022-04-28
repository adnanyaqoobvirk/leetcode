class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def possible() -> bool:
            stack, seen = [(0, 0)], {(0, 0)}
            while stack:
                i, j = stack.pop()
                if i == m - 1 and j == n - 1:
                    return True

                for x, y in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]:
                    if (
                        0 <= x < m and 0 <= y < n and
                        (x, y) not in seen and
                        abs(heights[x][y] - heights[i][j]) <= k
                    ):
                        seen.add((x, y))
                        stack.append((x, y))
            return False
                            
        m, n = len(heights), len(heights[0])
        lo, hi = 0, max(max(heights[i]) for i in range(m))
        while lo < hi:
            k = lo + (hi - lo) // 2
            if possible():
                hi = k
            else:
                lo = k + 1
        return lo
                