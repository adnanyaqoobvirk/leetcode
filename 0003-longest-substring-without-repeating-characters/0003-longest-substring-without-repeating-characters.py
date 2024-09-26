class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        char_counts = {}
        l = 0
        for r in range(len(s)):
            char_counts[s[r]] = char_counts.get(s[r], 0) + 1

            while l < r and char_counts[s[r]] > 1:
                char_counts[s[l]] -= 1

                if char_counts[s[l]] == 0:
                    del char_counts[s[l]]
                
                l += 1
            
            longest = max(longest, r - l + 1)
        return longest