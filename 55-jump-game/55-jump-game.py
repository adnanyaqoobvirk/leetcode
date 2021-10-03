class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right = len(nums) - 1
        left = right - 1
        while left >= 0:
            if (nums[left] - right + left) >= 0:
                right = left
                left -= 1
            else:
                left -= 1
        return False if right else True