class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
                
            if nums[i] > nums[i - 1]:
                if increasing == 0:
                    increasing = 1
                elif increasing != 1:
                    return False
            else:
                if increasing == 0:
                    increasing = -1
                elif increasing != -1:
                    return False
        return True
        