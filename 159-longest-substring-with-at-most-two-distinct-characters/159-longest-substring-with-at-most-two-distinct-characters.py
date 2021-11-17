class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        ans = i = 0
        while i < n:
            count = 0
            unique = set()
            second_char_start = None
            for j in range(i, n):
                unique.add(s[j])
                if len(unique) > 2:
                    break
                elif len(unique) == 2 and second_char_start is None:
                    second_char_start = j
                count += 1
            else:
                ans = max(ans, count)
                break
            ans = max(ans, count)
            i = i + 1 if second_char_start is None else second_char_start 
        return ans