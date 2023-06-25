class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        longest = l = 0
        counts = {}
        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            while len(counts) > k:
                counts[s[l]] -= 1
                if counts[s[l]] == 0:
                    del counts[s[l]]
                l += 1
            longest = max(longest, r - l + 1)
        return longest