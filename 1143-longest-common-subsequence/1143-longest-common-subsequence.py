class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dp(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0
            
            return max(
                dp(i, j - 1),
                dp(i - 1, j),
                (text1[i] == text2[j]) + dp(i - 1, j - 1)
            )
        
        n, m = len(text1), len(text2)
        return dp(n - 1, m - 1)