class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        @cache
        def dp(i: int, sa: bool) -> int:
            if i < 0:
                return 0 if sa else -inf
            
            if sa:
                return max(0, nums[i] + dp(i - 1, True))
            else:
                return max(nums[i] + dp(i - 1, True), dp(i - 1, False))
        return dp(len(nums) - 1, False)