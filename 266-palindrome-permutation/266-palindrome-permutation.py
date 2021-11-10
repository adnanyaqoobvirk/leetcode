class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        odds = 0
        for c, count in Counter(s).items():
            if count & 1:
                odds += 1
            
            if odds > 1:
                return False
        return True
                