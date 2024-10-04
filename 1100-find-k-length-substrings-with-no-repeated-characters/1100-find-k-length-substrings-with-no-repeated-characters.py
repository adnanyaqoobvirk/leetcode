class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        ans = 0
        seen = {}
        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                del seen[s[l]]
                l += 1
            seen[s[r]] = r
            
            if r - l + 1 == k:
                del seen[s[l]]
                l += 1
                ans += 1
        return ans