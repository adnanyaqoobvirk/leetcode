class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [0] * (n + 1)
        curr = [0] * (n + 1)
        curr[1] = 1
        for _ in range(m):
            for j in range(1, n + 1):
                curr[j] += prev[j] + curr[j - 1]
            prev, curr = curr, [0] * (n + 1)
        return prev[-1]