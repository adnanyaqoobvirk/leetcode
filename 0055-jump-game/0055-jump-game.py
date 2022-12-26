class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right = len(nums) - 1
        for i in reversed(range(right)):
            if nums[i] >= right - i:
                right = i
        return right == 0