class Solution:
    def removePalindromeSub(self, s: str) -> int:
        lo, hi = 0, len(s) - 1
        while lo < hi:
            if s[lo] != s[hi]:
                return 2
            lo, hi = lo + 1, hi - 1
        return 1