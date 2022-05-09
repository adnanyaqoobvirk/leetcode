class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = curr = 0
        for i in range(len(nums)):
            prev, curr = curr, max(nums[i] + prev, curr)
        return curr