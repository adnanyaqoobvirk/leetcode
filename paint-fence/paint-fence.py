class Solution:
    def numWays(self, n: int, k: int) -> int:
        prev, curr = k, k * k
        for pos in range(n - 1):
            prev, curr = curr, (k - 1) * (curr + prev)
        return prev