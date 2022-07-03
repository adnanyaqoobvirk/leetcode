class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        prev, curr = [0] * (n + 1), [0] * (n + 1)
        for p1 in reversed(range(n)):
            for p2 in range(1, n + 1):
                if s[p1] == s[p2 - 1]:
                    curr[p2] = 1 + prev[p2 - 1]
                else:
                    curr[p2] = max(
                        prev[p2],
                        curr[p2 - 1]
                    )
            prev, curr = curr, prev
        return prev[n]