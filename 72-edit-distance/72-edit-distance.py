class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def helper(p1: int, p2: int) -> int:
            if p1 == m and p2 == n:
                return 0
            
            if p1 == m:
                return n - p2
            
            if p2 == n:
                return m - p1
            
            if word1[p1] == word2[p2]:
                return helper(p1 + 1, p2 + 1)
            
            return 1 + min(
                helper(p1, p2 + 1),
                helper(p1 + 1, p2),
                helper(p1 + 1, p2 + 1)
            )
        m, n = len(word1), len(word2)
        return helper(0, 0)