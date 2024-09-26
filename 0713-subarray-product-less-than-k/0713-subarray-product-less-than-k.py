class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        sub_count = 0
        curr_product = 1
        l = 0
        for r in range(len(nums)):
            curr_product *= nums[r]

            while l < r and curr_product >= k:
                curr_product /= nums[l]
                l += 1
            
            if curr_product < k:
                sub_count += r - l + 1
        return sub_count