class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = 0
        for i, num in enumerate(nums):
            if prefix == total - prefix - num:
                return i
            prefix += num
        return -1