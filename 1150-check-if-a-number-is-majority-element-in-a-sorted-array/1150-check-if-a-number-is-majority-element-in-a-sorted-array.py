class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] < target:
                left += 1
            elif nums[right] > target:
                right -= 1
            else:
                break
        return right - left + 1 > len(nums) // 2