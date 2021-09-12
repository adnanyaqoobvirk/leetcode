class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n = x^y
        ans = 0
        while n > 0:
            ans += n & 1
            n >>= 1
        return ans