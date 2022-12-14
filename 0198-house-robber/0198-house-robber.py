class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def helper(pos):
            if pos >= n:
                return 0
            
            return max(
                nums[pos] + helper(pos + 2),
                helper(pos + 1)
            )
        n = len(nums)
        return helper(0)