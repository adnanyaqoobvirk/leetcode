class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n = x^y
        ans = 0
        while n > 0:
            if n & 1:
                ans += 1
            n = n >> 1
        return ans