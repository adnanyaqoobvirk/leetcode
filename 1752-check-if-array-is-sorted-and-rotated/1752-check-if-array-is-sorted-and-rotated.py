class Solution:
    def check(self, nums: List[int]) -> bool:
        icount = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                icount += 1
        if nums[0] < nums[len(nums) - 1]:
            icount += 1
        return icount <= 1