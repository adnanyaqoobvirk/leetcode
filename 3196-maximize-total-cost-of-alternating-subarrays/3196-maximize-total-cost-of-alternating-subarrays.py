class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        @cache
        def dp(i: int, even: bool) -> int:
            if i >= n:
                return 0
            
            return max(
                (-nums[i] if even else nums[i]) + dp(i + 1, not even),
                nums[i] + dp(i + 1, True)
            )
        n = len(nums)
        return nums[0] + dp(1, True)