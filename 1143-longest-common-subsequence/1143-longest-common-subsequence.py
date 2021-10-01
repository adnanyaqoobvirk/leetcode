class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def recurse(i: int, j: int) -> int:
            if i == len(text1) or j == len(text2):
                return 0
                
            return max(
                recurse(i, j + 1), 
                recurse(i + 1, j), 
                int(text1[i] == text2[j]) + recurse(i + 1, j + 1)
            )
        
        return recurse(0, 0)