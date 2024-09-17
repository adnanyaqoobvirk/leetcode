from sortedcontainers import SortedList

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        max_sum = -inf
        for col in range(n):
            dp = [0] * m
            for j in range(col, n):
                for i in range(m):
                    dp[i] += matrix[i][j]
                
                curr_sum = -inf
                curr_max = -inf
                for a in range(m):
                    curr_sum = max(dp[a], dp[a] + curr_sum)
                    curr_max = max(curr_max, curr_sum)
                if curr_max <= k:
                    max_sum = max(max_sum, curr_max)
                    continue
                
                presums = SortedList([0])
                curr_sum = 0
                for a in range(m):
                    curr_sum += dp[a]
                    idx = presums.bisect_left(curr_sum - k)
                    if idx < len(presums):
                        max_sum = max(max_sum, curr_sum - presums[idx])
                    presums.add(curr_sum)
        return max_sum