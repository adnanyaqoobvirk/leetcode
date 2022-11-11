class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        k = left = 1
        for right in range(1, n):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
                k += 1
        return k