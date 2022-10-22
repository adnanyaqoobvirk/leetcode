class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        seen = set()
        for c in s:
            if c in seen:
                ans += 2
                seen.remove(c)
            else:
                seen.add(c)
        return ans + 1 if seen else ans