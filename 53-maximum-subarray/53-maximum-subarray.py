class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        curr_picked, curr_not_picked = 0, -inf
        for pos in reversed(range(n)):
            curr_picked, curr_not_picked = max(
                nums[pos] + curr_picked,
                0
            ), max(
                nums[pos] + curr_picked,
                curr_not_picked
            )
        return curr_not_picked
            
            