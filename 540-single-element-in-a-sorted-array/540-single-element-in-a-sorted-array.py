class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid - 1] == nums[mid]:
                if (mid - 1 - left) & 1:
                    right = mid - 2
                else:
                    left = mid + 1
            elif nums[mid + 1] == nums[mid]:
                if (mid - left) & 1:
                    right = mid - 1
                else:
                    left = mid + 2
            else:
                left = right = mid
        return nums[left]