class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        max_pd = s[0]
        for i in range(1, n):
            left = right = i
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            
            if (right - left - 1) > len(max_pd):
                max_pd = s[left + 1:right]
            
            left, right = i - 1, i
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            
            if (right - left - 1) > len(max_pd):
                max_pd = s[left + 1:right]
        return max_pd