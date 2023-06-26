class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        mid = False
        for freq in Counter(s).values():
            if freq & 1:
                if mid:
                    return False
                mid = True
        return True