class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        max_len = 1
        rep_idx = -1
        l = 0
        for r in range(1, len(s)):
            if s[r] == s[r - 1]:
                if rep_idx > -1:
                    l = rep_idx + 1
                rep_idx = r - 1

            max_len = max(max_len, r - l + 1)
        return max_len

            