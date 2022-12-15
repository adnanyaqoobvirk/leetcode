class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def helper(p1, p2):
            if p1 >= m or p2 >= n:
                return 0
            
            return max(
                helper(p1 + 1, p2),
                helper(p1, p2 + 1),
                (text1[p1] == text2[p2]) + helper(p1 + 1, p2 + 1)
            )
        m, n = len(text1), len(text2)
        return helper(0, 0)