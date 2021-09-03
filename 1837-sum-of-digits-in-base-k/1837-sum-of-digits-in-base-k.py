class Solution:
    def sumBase(self, n: int, k: int) -> int:
        ans = 0
        while n > 0:
            n, d = divmod(n, k)
            ans += d
        return ans