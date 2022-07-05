class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for remaining in range(target + 1):
            for num in nums:
                if remaining - num < 0:
                    continue
                dp[remaining] += dp[remaining - num]
        return dp[target]