class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        one_count_exists = False
        for c, cnt in Counter(s).items():
            if cnt & 1:
                one_count_exists = True
                cnt -= 1
                
            ans += cnt 
        return ans + 1 if one_count_exists else ans