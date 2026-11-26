class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        distinct = {}
        l = 0
        max_len = 0
        for r in range(len(s)):
            if s[r] not in distinct:
                distinct[s[r]] = 1
            else:
                distinct[s[r]] += 1
            
            while len(distinct) > k:
                distinct[s[l]] -= 1
                if distinct[s[l]] == 0:
                    del distinct[s[l]]
                l += 1
            
            max_len = max(max_len, r - l + 1)
        return max_len