class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left + len(nums) // 2 < len(nums) and target == nums[left + len(nums) // 2]