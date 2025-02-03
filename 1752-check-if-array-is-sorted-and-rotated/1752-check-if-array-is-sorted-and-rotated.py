class Solution:
    def check(self, nums: List[int]) -> bool:
        icount = 0
        max_val = 0
        for i in range(1, len(nums)):
            if icount > 0 and nums[i] > max_val:
                return False

            if nums[i - 1] > nums[i]:
                max_val = nums[0]
                icount += 1
                
            if icount > 1:
                return False
        return True