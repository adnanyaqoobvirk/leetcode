class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        prev, curr = [triangle[n - 1][col] for col in range(n)], [0] * n
        for row in reversed(range(n - 1)):
            for col in reversed(range(row + 1)):
                curr[col] = triangle[row][col] + min(
                    prev[col],
                    prev[col + 1]
                )
            prev, curr = curr, prev
        return prev[0]