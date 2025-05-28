class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot = sum(nums)
        curr = 0
        for i in range(len(nums)):
            if tot - nums[i] - curr == curr:
                return i
            curr += nums[i]
        return -1