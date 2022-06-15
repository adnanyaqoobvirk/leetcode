class Solution:
    def fib(self, n: int) -> int:
        prev, curr = 0, 1
        for _ in range(n):
            prev, curr = curr, curr + prev
        return prev