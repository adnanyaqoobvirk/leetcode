class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dp(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0
            
            if text1[i] == text2[j]:
                ans = 1 + dp(i - 1, j - 1)
            else:
                ans = max(
                    dp(i, j - 1),
                    dp(i - 1, j)
                )
            return ans
        return dp(len(text1) - 1, len(text2) - 1)