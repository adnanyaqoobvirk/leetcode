class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        longest = s[0]
        for i in range(n):
            left, right = i - 1, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            
            if len(longest) < (right - left - 1):
                longest = s[left + 1:right]
            
            if i + 1 < n and s[i] == s[i + 1]:
                left, right = i - 1, i + 2
                while left >= 0 and right < n and s[left] == s[right]:
                    left -= 1
                    right += 1

                if len(longest) < (right - left - 1):
                    longest = s[left + 1:right]
        return longest