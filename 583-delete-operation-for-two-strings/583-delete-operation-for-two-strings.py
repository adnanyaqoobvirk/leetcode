class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def helper(p1: int, p2: int) -> int:
            if p1 == m:
                return n - p2
            
            if p2 == n:
                return m - p1
            
            return min(
                1 + helper(p1 + 1, p2),
                1 + helper(p1, p2 + 1),
                helper(p1 + 1, p2 + 1) if word1[p1] == word2[p2] else inf
            )
        
        m, n = len(word1), len(word2)
        return helper(0, 0)