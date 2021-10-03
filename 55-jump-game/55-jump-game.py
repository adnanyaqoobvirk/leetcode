class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right = len(nums) - 1
        for left in range(len(nums) - 2, -1, -1):
            if nums[left] - right + left >= 0:
                right = left
        return False if right else True