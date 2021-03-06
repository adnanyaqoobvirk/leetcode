class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev, curr = [0] * (n + 1), [0] * (n + 1)
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if i == m - 1 and j == n - 1:
                    curr[j] = 1
                else:
                    curr[j] = prev[j] + curr[j + 1]
            prev, curr = curr, prev
        return prev[0]