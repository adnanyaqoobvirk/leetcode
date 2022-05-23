class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        prev, curr = [0] * (n + 1), [0] * (n + 1)
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                curr[j] = max(
                    (prev[j + 1] + 1) if text1[i] == text2[j] else 0,
                    prev[j],
                    curr[j + 1]
                )
            prev, curr = curr, prev
        return prev[0]