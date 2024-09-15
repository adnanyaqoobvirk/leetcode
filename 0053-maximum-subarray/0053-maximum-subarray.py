class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = 0
        curr_sum = 0
        for num in nums:
            curr_sum = max(curr_sum + num, num)
            ans = max(ans, curr_sum)
        return ans