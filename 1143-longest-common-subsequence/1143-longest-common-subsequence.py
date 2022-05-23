class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def helper(i: int, j: int) -> int:
            if i >= m or j >= n:
                return 0
            
            return max(
                (helper(i + 1, j + 1) + 1) if text1[i] == text2[j] else 0,
                helper(i + 1, j),
                helper(i, j + 1)
            )
        
        m, n = len(text1), len(text2)
        return helper(0, 0)
        