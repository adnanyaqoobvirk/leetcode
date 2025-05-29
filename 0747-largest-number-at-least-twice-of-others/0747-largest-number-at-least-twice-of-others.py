class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        mx_idx = 0
        for i in range(len(nums)):
            if nums[i] >= nums[mx_idx]:
                mx_idx = i
        for i in range(len(nums)):
            if mx_idx != i and nums[mx_idx] < 2 * nums[i]:
                return -1
        return mx_idx