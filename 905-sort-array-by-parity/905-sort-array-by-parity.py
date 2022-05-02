class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            if (nums[left] & 1) and (not nums[right] & 1):
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            elif nums[right] & 1:
                right -= 1
            else:
                left += 1
        return nums