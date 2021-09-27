class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        left, right = -1, len(nums)
        left_sum = right_sum = 0
        while left < right:
            if left_sum > right_sum:
                right -= 1
                right_sum += nums[right]
            else:
                left += 1
                left_sum += nums[left]
        return nums[:left + 1]