class Solution:
    def numSub(self, s: str) -> int:
        ans = 0
        ones = 0
        for r in range(len(s)):
            if s[r] == '0':
                ones = 0
            else:
                ones += 1
                ans += ones
        return ans % (10**9 + 7)
