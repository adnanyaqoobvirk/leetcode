class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = 1
        for i in range(1, m):
            res *= (n - 1 + i) / i
        return int(res) + 1 if res - int(res) >= 0.5 else int(res)