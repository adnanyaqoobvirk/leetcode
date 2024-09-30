class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        max_freq = 0
        curr_sum = 0
        l = 0
        for r in range(len(nums)):
            curr_sum += nums[r]

            while l < r and (r - l + 1) * nums[r] - curr_sum > k:
                curr_sum -= nums[l]
                l += 1
            
            max_freq = max(max_freq, r - l + 1)
        return max_freq