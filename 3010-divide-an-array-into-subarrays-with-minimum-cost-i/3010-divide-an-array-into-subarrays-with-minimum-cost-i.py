class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first_min = second_min = inf
        for i in range(1, len(nums)):
            if nums[i] < first_min:
                second_min, first_min = first_min, nums[i]
            elif nums[i] < second_min:
                second_min = nums[i]
        return nums[0] + first_min + second_min