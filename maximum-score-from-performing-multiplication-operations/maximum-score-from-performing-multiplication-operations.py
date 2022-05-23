class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        for i in reversed(range(m)):
            for left in reversed(range(i + 1)):
                right = n - 1 - (i - left)
                dp[i][left] = max(
                    nums[left] * multipliers[i] + dp[i + 1][left + 1],
                    nums[right] * multipliers[i] + dp[i + 1][left]
                )
        return dp[0][0]