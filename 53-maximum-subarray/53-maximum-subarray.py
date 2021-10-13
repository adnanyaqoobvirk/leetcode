class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = float('-inf')
        curr = 0
        for num in nums:
            if curr < 0:
                curr = 0
            curr += num
            mx = max(curr, mx)
        return mx