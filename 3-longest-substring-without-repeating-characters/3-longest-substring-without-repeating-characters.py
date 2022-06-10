class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_idx_map = {}
        left = longest = 0
        for right in range(len(s)):
            if s[right] in char_idx_map:
                left = max(char_idx_map[s[right]] + 1, left)
            char_idx_map[s[right]] = right
            longest = max(longest, right - left + 1)
        return longest