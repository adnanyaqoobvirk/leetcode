class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        prev_row = [0] * (m + 1)
        curr_row = [0]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                curr_row.append(
                    max(
                        curr_row[j - 1],
                        prev_row[j],
                        int(text1[i - 1] == text2[j - 1]) + prev_row[j - 1]
                    )
                )
            prev_row, curr_row = curr_row, [0] 
        return prev_row[-1]