class Solution:
    def tribonacci(self, n: int) -> int:
        t0, t1, t2 = 0, 1, 1
        for i in range(n):
            t0, t1, t2 = t1, t2, t2 + t1 + t0
        return t0