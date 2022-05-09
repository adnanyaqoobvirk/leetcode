class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def helper(pos: int) -> int:
            if pos < 0:
                return 0
            
            return max(
                nums[pos] + helper(pos - 2),
                helper(pos - 1)
            )
        n = len(nums)
        return helper(n - 1)
        