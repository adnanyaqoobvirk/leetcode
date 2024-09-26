class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        chars = defaultdict(int)
        max_char = '?'
        l = 0
        for r in range(len(s)):
            chars[s[r]] += 1
            if chars[max_char] < chars[s[r]]:
                max_char = s[r]
            
            if r - l + 1 - chars[max_char] > k:
                chars[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        return longest