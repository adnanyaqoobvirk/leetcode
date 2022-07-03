class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def helper(p1: int, p2: int) -> int:
            if p1 == n or p2 == -1:
                return 0
            
            if s[p1] == s[p2]:
                return 1 + helper(p1 + 1, p2 - 1)
            else:
                return max(
                    helper(p1 + 1, p2),
                    helper(p1, p2 - 1)
                )
        n = len(s)
        return helper(0, n - 1)
        