class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 0
        curr = 1
        for _ in range(1, n + 1):
            prev, curr = curr, prev + curr
        return curr