class Solution:
    def integerBreak(self, n: int) -> int:
        curr = [-inf] * (n + 1)
        curr[0] = 1
        for num in reversed(range(1, n)):
            for remaining in range(num, n + 1):
                curr[remaining] = max(
                    num * curr[remaining - num],
                    curr[remaining]
                )
        return curr[n]