class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n = x^y
        ans = 0
        while n > 0:
            ans += 1
            n = n & n - 1
        return ans