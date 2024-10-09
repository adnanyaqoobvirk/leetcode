class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        chars = {}
        max_len = 0
        l = 0
        for r in range(len(s)):
            chars[s[r]] = chars.get(s[r], 0) + 1

            while l <= r and len(chars) > k:
                chars[s[l]] -= 1
                if chars[s[l]] == 0:
                    del chars[s[l]]
                l += 1
            
            max_len = max(max_len, r - l + 1)
        return max_len