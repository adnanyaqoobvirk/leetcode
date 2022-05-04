class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        ops, left, right = 0, 0, len(nums) - 1
        while left < right:
            total = nums[left] + nums[right]
            if total > k:
                right -= 1
            elif total < k:
                left += 1
            else:
                right -= 1
                left += 1
                ops += 1
        return ops