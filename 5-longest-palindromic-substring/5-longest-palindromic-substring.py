class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        max_pd = s[0]
        for i in range(1, n):
            left = right = i
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            
            pd = s[left + 1:right]
            if len(pd) > len(max_pd):
                max_pd = pd
            
            left, right = i - 1, i
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            
            pd = s[left + 1:right]
            if len(pd) > len(max_pd):
                max_pd = pd
        return max_pd