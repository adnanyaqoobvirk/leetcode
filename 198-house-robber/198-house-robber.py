class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def helper(pos: int) -> int:
            if pos >= len(nums):
                return 0
            
            return max(
                nums[pos] + helper(pos + 2),
                helper(pos + 1)
            )
        return helper(0)