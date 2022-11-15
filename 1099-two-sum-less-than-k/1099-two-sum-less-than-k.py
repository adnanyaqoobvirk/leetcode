class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        max_total = -1
        left, right = 0, len(nums) - 1
        while left < right:
            total = nums[left] + nums[right]
            if total >= k:
                right -= 1
            else:
                max_total = max(max_total, total)
                left += 1
        return max_total