class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        maxLen = 0
        l = 0
        cost = 0
        for r in range(len(s)):
            if s[r] != t[r]:
                cost += abs(ord(s[r]) - ord(t[r]))

            while l <= r and cost > maxCost:
                cost -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            
            maxLen = max(maxLen, r - l + 1)
        return maxLen