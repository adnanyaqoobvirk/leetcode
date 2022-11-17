class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        p = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[p]:
                break
            p = i
        return p