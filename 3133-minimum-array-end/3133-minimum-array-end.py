class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n = n - 1
        p = 1
        while n > 0:
            while x & p:
                p <<= 1
            if n & 1:
                x |= p
            p <<= 1
            n >>= 1
        return x