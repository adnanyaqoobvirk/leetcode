class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        for num in nums:
            a = num % k
            for b in range(k):
                dp[a][b] = max(dp[a][b], 1 + dp[b][a])
        return max(max(dp[i]) for i in range(k))