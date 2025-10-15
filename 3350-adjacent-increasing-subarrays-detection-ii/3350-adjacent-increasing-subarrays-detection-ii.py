class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        ans, prev, curr = 1, 0, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr += 1
            else:
                prev, curr = curr, 1
            ans = max(ans, min(prev, curr), curr // 2)
        return ans