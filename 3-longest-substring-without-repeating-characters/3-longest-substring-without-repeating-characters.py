class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_idx_map = defaultdict(lambda: -1)
        left = longest = 0
        for right in range(len(s)):
            if char_idx_map[s[right]] != -1:
                duplicate_idx = char_idx_map[s[right]]
                for i in range(left, duplicate_idx + 1):
                    if char_idx_map[s[i]] <= duplicate_idx:
                        del char_idx_map[s[i]]
                left = duplicate_idx + 1
            char_idx_map[s[right]] = right
            longest = max(longest, right - left + 1)
        return longest