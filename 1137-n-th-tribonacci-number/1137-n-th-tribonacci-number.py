class Solution:
    def tribonacci(self, n: int) -> int:
        t0, t1, t2 = 0, 1, 1
        for i in range(3, n + 1):
            t0, t1, t2 = t1, t2, t2 + t1 + t0
        return t0 if n == 0 else (t1 if n == 1 else t2)