class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        k_min_sum = [inf] * k
        k_min_sum[0] = 0
        curr_sum = 0
        max_sum = -inf
        for i in range(len(nums)):
            curr_sum += nums[i]
            j = (i + 1) % k
            max_sum = max(max_sum, curr_sum - k_min_sum[j])
            k_min_sum[j] = min(k_min_sum[j], curr_sum)
        return max_sum