class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            count = 0
            unique = set()
            for j in range(i, len(s)):
                unique.add(s[j])
                if len(unique) > 2:
                    break
                count += 1
            ans = max(ans, count)
        return ans