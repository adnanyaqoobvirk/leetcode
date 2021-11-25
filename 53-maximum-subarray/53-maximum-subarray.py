class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = float('-inf')
        curr = 0
        for num in nums:
            curr += num
            if curr < num:
                curr = num
            maximum = max(curr, maximum)
        return maximum