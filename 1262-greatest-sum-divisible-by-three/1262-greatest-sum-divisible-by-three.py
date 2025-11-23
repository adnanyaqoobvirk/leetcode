class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        @cache
        def dp(i: int, total: int) -> int:
            if i >= n:
                if total == 0:
                    return 0
                else:
                    return -inf

            return max(
                nums[i] + dp(i + 1, (total + nums[i]) % 3),
                dp(i + 1, total)
            )
        n = len(nums)
        return dp(0, 0)