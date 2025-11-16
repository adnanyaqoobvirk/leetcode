class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        ans = 0
        ones = 0
        for r in range(len(s)):
            if s[r] == '0':
                ones = 0
            else:
                ones += 1
                ans += ones
                ans %= MOD
        return ans
