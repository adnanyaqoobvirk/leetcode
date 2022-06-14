class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        prev, curr = [inf] * (n + 1), [inf] * (n + 1)
        for p1 in reversed(range(m + 1)):
            for p2 in reversed(range(n + 1)):
                if p1 == m:
                    curr[p2] = n - p2
                elif p2 == n:
                    curr[p2] = m - p1
                else:
                    curr[p2] = min(
                        1 + prev[p2],
                        1 + curr[p2 + 1],
                        prev[p2 + 1] if word1[p1] == word2[p2] else inf
                    )
            prev, curr = curr, [inf] * (n + 1)
        return prev[0]