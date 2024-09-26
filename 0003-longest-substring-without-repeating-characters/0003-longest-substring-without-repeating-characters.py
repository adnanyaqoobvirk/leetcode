class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        chars = {}
        l = 0
        for r in range(len(s)):
            if s[r] in chars:
                l = max(l, chars[s[r]] + 1)
            chars[s[r]] = r
            longest = max(longest, r - l + 1)
        return longest