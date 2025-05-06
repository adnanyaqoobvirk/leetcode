class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            v = nums[nums[i] & 0xFFFF] & 0xFFFF
            nums[i] |= v << 16
        for i in range(len(nums)):
            nums[i] = nums[i] >> 16
        return nums