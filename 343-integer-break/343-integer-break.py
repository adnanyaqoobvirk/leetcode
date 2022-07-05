class Solution:
    def integerBreak(self, n: int) -> int:
        prev, curr = [-inf] * (n + 1), [-inf] * (n + 1)
        prev[0] = 1
        for num in reversed(range(1, n)):
            for remaining in range(n + 1):
                if remaining - num < 0:
                    curr[remaining] = prev[remaining]
                else:
                    curr[remaining] = max(
                        num * curr[remaining - num],
                        prev[remaining]
                    )
            prev, curr = curr, prev
        return prev[n]