class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min_cost = nums[0]
        first_min = inf
        second_min = inf
        for i in range(1, len(nums)):
            if nums[i] < first_min:
                second_min = min(second_min, first_min)
                first_min = nums[i]
            elif nums[i] < second_min:
                second_min = nums[i]
        return min_cost + first_min + second_min