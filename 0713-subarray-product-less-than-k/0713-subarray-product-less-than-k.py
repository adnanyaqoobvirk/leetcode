class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 0:
            return 0

        nums = [log(num) for num in nums]
        k = log(k)
        error = -1e-9
        sub_count = 0
        curr_sum = 0
        l = 0
        for r in range(len(nums)):
            curr_sum += nums[r]

            while curr_sum - k >= error:
                curr_sum -= nums[l]
                l += 1
            
            sub_count += r - l + 1
        return sub_count