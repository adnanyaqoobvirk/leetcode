class Solution:
    def minOperations(self, nums: List[int]) -> int:
        max_val = nums[0]
        total = 0
        for i in range(1, len(nums)):
            if nums[i] <= max_val:
                ops = max_val - nums[i] + 1
                total += ops
                max_val = nums[i] + ops
            else:
                max_val = nums[i]
        return total