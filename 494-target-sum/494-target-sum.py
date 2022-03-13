class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def helper(i: int, total: int) -> int:
            if i == len(nums):
                return total == target
            
            return helper(i + 1, total + nums[i]) + helper(i + 1, total - nums[i])           
        return helper(0, 0)